#!/usr/bin/env python3
"""
Sincronización de métricas de Google Analytics 4 para OKRs
Colombiatours Growth Team
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
import requests
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GA4Sync:
    """Sincronizador de métricas de Google Analytics 4"""
    
    def __init__(self):
        self.property_id = os.environ.get('GA4_PROPERTY_ID')
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo = os.environ.get('GITHUB_REPOSITORY', 'ColombiaTours-Travel/growth-system')
        
        # Inicializar cliente GA4
        self.client = BetaAnalyticsDataClient()
        
        # Métricas OKR mapeadas
        self.okr_metrics = {
            'organic_traffic': {
                'ga4_metric': 'sessions',
                'dimension': 'sessionSource',
                'filter': 'organic',
                'okr_id': 'KR1.1'
            },
            'conversion_rate': {
                'ga4_metric': 'conversions',
                'secondary_metric': 'sessions',
                'okr_id': 'KR2.1'
            },
            'cart_abandonment': {
                'ga4_metric': 'purchaseRevenue',
                'events': ['add_to_cart', 'begin_checkout', 'purchase'],
                'okr_id': 'KR2.2'
            },
            'average_order_value': {
                'ga4_metric': 'averagePurchaseRevenue',
                'okr_id': 'KR2.3'
            }
        }

    def fetch_ga4_metrics(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """Obtener métricas de GA4"""
        
        metrics_data = {}
        
        try:
            # Tráfico orgánico internacional
            organic_request = RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                dimensions=[
                    Dimension(name="sessionSource"),
                    Dimension(name="country")
                ],
                metrics=[
                    Metric(name="sessions"),
                    Metric(name="activeUsers"),
                    Metric(name="screenPageViews")
                ],
                dimension_filter={
                    "and_group": {
                        "expressions": [
                            {
                                "filter": {
                                    "field_name": "sessionSource",
                                    "string_filter": {
                                        "match_type": "CONTAINS",
                                        "value": "organic"
                                    }
                                }
                            },
                            {
                                "not_expression": {
                                    "filter": {
                                        "field_name": "country",
                                        "string_filter": {
                                            "match_type": "EXACT",
                                            "value": "Colombia"
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            )
            
            organic_response = self.client.run_report(organic_request)
            
            # Procesar respuesta de tráfico orgánico
            total_organic_sessions = 0
            for row in organic_response.rows:
                total_organic_sessions += int(row.metric_values[0].value)
            
            metrics_data['organic_traffic_international'] = total_organic_sessions
            
            # Tasa de conversión
            conversion_request = RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                metrics=[
                    Metric(name="sessions"),
                    Metric(name="conversions"),
                    Metric(name="purchaseRevenue"),
                    Metric(name="transactions")
                ]
            )
            
            conversion_response = self.client.run_report(conversion_request)
            
            if conversion_response.rows:
                sessions = int(conversion_response.rows[0].metric_values[0].value)
                conversions = int(conversion_response.rows[0].metric_values[1].value)
                revenue = float(conversion_response.rows[0].metric_values[2].value)
                transactions = int(conversion_response.rows[0].metric_values[3].value)
                
                conversion_rate = (conversions / sessions * 100) if sessions > 0 else 0
                avg_order_value = (revenue / transactions) if transactions > 0 else 0
                
                metrics_data['conversion_rate'] = round(conversion_rate, 2)
                metrics_data['average_order_value'] = round(avg_order_value, 2)
                metrics_data['total_sessions'] = sessions
                metrics_data['total_revenue'] = round(revenue, 2)
            
            # Abandono de carrito (funnel)
            funnel_request = RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                dimensions=[Dimension(name="eventName")],
                metrics=[Metric(name="eventCount")],
                dimension_filter={
                    "or_group": {
                        "expressions": [
                            {"filter": {"field_name": "eventName", "string_filter": {"value": "add_to_cart"}}},
                            {"filter": {"field_name": "eventName", "string_filter": {"value": "begin_checkout"}}},
                            {"filter": {"field_name": "eventName", "string_filter": {"value": "purchase"}}}
                        ]
                    }
                }
            )
            
            funnel_response = self.client.run_report(funnel_request)
            
            funnel_data = {}
            for row in funnel_response.rows:
                event_name = row.dimension_values[0].value
                event_count = int(row.metric_values[0].value)
                funnel_data[event_name] = event_count
            
            # Calcular tasa de abandono
            if 'add_to_cart' in funnel_data and 'purchase' in funnel_data:
                cart_abandonment = (1 - (funnel_data['purchase'] / funnel_data['add_to_cart'])) * 100
                metrics_data['cart_abandonment_rate'] = round(cart_abandonment, 2)
            
            # Métricas por país para mercados target
            country_request = RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                dimensions=[Dimension(name="country")],
                metrics=[
                    Metric(name="activeUsers"),
                    Metric(name="conversions"),
                    Metric(name="purchaseRevenue")
                ],
                dimension_filter={
                    "or_group": {
                        "expressions": [
                            {"filter": {"field_name": "country", "string_filter": {"value": "Mexico"}}},
                            {"filter": {"field_name": "country", "string_filter": {"value": "Spain"}}},
                            {"filter": {"field_name": "country", "string_filter": {"value": "United States"}}}
                        ]
                    }
                }
            )
            
            country_response = self.client.run_report(country_request)
            
            metrics_data['country_metrics'] = {}
            for row in country_response.rows:
                country = row.dimension_values[0].value
                metrics_data['country_metrics'][country] = {
                    'users': int(row.metric_values[0].value),
                    'conversions': int(row.metric_values[1].value),
                    'revenue': float(row.metric_values[2].value)
                }
            
            logger.info(f"Métricas GA4 obtenidas exitosamente: {metrics_data}")
            return metrics_data
            
        except Exception as e:
            logger.error(f"Error obteniendo métricas GA4: {e}")
            return {}

    def update_github_issues(self, metrics: Dict[str, Any]):
        """Actualizar issues de GitHub con métricas"""
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # Mapeo de métricas a issues
        metric_issue_map = {
            'organic_traffic_international': {
                'issue_title': '[KR] Aumentar tráfico orgánico internacional',
                'metric_key': 'organic_traffic_international',
                'format': '{:,}'
            },
            'conversion_rate': {
                'issue_title': '[KR] Aumentar conversión web',
                'metric_key': 'conversion_rate',
                'format': '{:.2f}%'
            },
            'cart_abandonment_rate': {
                'issue_title': '[KR] Reducir abandono de carrito',
                'metric_key': 'cart_abandonment_rate',
                'format': '{:.1f}%'
            },
            'average_order_value': {
                'issue_title': '[KR] Incrementar ticket promedio',
                'metric_key': 'average_order_value',
                'format': '${:,.2f}'
            }
        }
        
        # Buscar y actualizar issues
        for metric_name, config in metric_issue_map.items():
            if config['metric_key'] in metrics:
                value = metrics[config['metric_key']]
                
                # Buscar issue por título
                search_url = f"https://api.github.com/repos/{self.repo}/issues"
                params = {
                    'state': 'open',
                    'labels': 'key-result'
                }
                
                response = requests.get(search_url, headers=headers, params=params)
                
                if response.status_code == 200:
                    issues = response.json()
                    
                    for issue in issues:
                        if config['issue_title'] in issue['title']:
                            # Actualizar comentario con métrica actual
                            comment_body = f"""
## 📊 Actualización Automática de Métricas

**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

### Métrica Actual
**Valor:** {config['format'].format(value)}

### Datos Adicionales
- **Período:** Últimos 30 días
- **Fuente:** Google Analytics 4
- **Actualización:** Automática diaria

---
*Este comentario fue generado automáticamente por el sistema de sincronización de OKRs*
                            """
                            
                            comment_url = f"{issue['url']}/comments"
                            requests.post(comment_url, headers=headers, json={'body': comment_body})
                            
                            logger.info(f"Issue actualizado: {issue['title']} con valor {value}")

    def save_metrics_json(self, metrics: Dict[str, Any]):
        """Guardar métricas en archivo JSON para otros procesos"""
        
        output_file = 'metrics-latest.json'
        
        metrics_output = {
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'period': {
                'start': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
                'end': datetime.now().strftime('%Y-%m-%d')
            }
        }
        
        with open(output_file, 'w') as f:
            json.dump(metrics_output, f, indent=2)
        
        logger.info(f"Métricas guardadas en {output_file}")

    def run(self):
        """Ejecutar sincronización completa"""
        
        logger.info("Iniciando sincronización de métricas GA4...")
        
        # Calcular período (últimos 30 días)
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        # Obtener métricas
        metrics = self.fetch_ga4_metrics(start_date, end_date)
        
        if metrics:
            # Guardar en JSON
            self.save_metrics_json(metrics)
            
            # Actualizar GitHub Issues
            self.update_github_issues(metrics)
            
            logger.info("Sincronización completada exitosamente")
            
            # Imprimir resumen
            print("\n📊 RESUMEN DE MÉTRICAS SINCRONIZADAS")
            print("=" * 50)
            print(f"Tráfico Orgánico Internacional: {metrics.get('organic_traffic_international', 0):,} sesiones")
            print(f"Tasa de Conversión: {metrics.get('conversion_rate', 0):.2f}%")
            print(f"Abandono de Carrito: {metrics.get('cart_abandonment_rate', 0):.1f}%")
            print(f"Ticket Promedio: ${metrics.get('average_order_value', 0):,.2f}")
            print("\n📍 Métricas por País:")
            
            for country, data in metrics.get('country_metrics', {}).items():
                print(f"  {country}:")
                print(f"    - Usuarios: {data['users']:,}")
                print(f"    - Conversiones: {data['conversions']}")
                print(f"    - Revenue: ${data['revenue']:,.2f}")
        else:
            logger.error("No se pudieron obtener métricas")
            return 1
        
        return 0

if __name__ == "__main__":
    syncer = GA4Sync()
    exit(syncer.run())