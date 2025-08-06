# 🚀 Colombiatours Growth - Sistema de Gestión OKR

> Sistema completo de gestión de OKRs, proyectos y equipos para el área de Growth de Colombiatours.travel usando GitHub Projects.

## 📊 Dashboard Status Q1 2025

| Objetivo | Progreso | Estado | Owner |
|----------|----------|--------|-------|
| 🎯 Dominar Tráfico Orgánico Internacional | 15% | 🟢 On Track | @seo-lead |
| 🎯 Optimización Máxima de Conversión | 8% | 🟡 At Risk | @cro-lead |
| 🎯 Expansión Mercados Prioritarios | 22% | 🟢 On Track | @growth-lead |

## 🏗️ Estructura del Sistema

### Proyectos GitHub

1. **[Growth OKRs 2025](../../projects/1)** - Gestión de objetivos y resultados clave
2. **[Growth Team Management](../../projects/2)** - Gestión de equipos y capacidad
3. **[Growth Initiatives](../../projects/3)** - Ejecución de iniciativas y tareas

### Vistas Disponibles

- **📈 OKR Dashboard** - Vista general de objetivos y progreso
- **👥 Team Workload** - Carga de trabajo por equipo
- **🗓️ Roadmap** - Timeline trimestral
- **📊 Metrics** - Métricas y KPIs en tiempo real

## 🎯 OKRs Q1 2025

### Objetivo 1: Dominar Tráfico Orgánico Internacional
**Owner:** @seo-lead | **Status:** 🟢 On Track | **Progress:** 15%

**Key Results:**
- KR1.1: Aumentar tráfico orgánico a 75K sesiones/mes (actual: 50K)
- KR1.2: Posicionar 25 keywords "Colombia tourism" en Top 3
- KR1.3: Mejorar CTR orgánico de 2.5% a 4.5%

### Objetivo 2: Optimización Máxima de Conversión
**Owner:** @cro-lead | **Status:** 🟡 At Risk | **Progress:** 8%

**Key Results:**
- KR2.1: Aumentar conversión web de 1.2% a 3%
- KR2.2: Reducir abandono de carrito de 70% a 40%
- KR2.3: Incrementar ticket promedio de $800 a $1,500 USD

### Objetivo 3: Expansión Mercados Prioritarios
**Owner:** @growth-lead | **Status:** 🟢 On Track | **Progress:** 22%

**Key Results:**
- KR3.1: Captar 600 nuevos clientes de México
- KR3.2: Generar $250K USD en revenue desde España
- KR3.3: Conseguir 100 nuevos clientes de USA

## 🚦 Quick Start

### 1. Crear un nuevo OKR
```bash
# Usar el template de issue
gh issue create --template okr-objetivo.yml
```

### 2. Actualizar métricas
```bash
# Ejecutar script de sincronización
python scripts/sync-analytics.py
```

### 3. Generar reporte semanal
```bash
# Generar y enviar reporte
python scripts/generate-reports.py --week current
```

## 📋 Templates Disponibles

- [🎯 OKR Objetivo](.github/ISSUE_TEMPLATE/1-okr-objetivo.yml)
- [📊 Key Result](.github/ISSUE_TEMPLATE/2-key-result.yml)
- [💡 Iniciativa](.github/ISSUE_TEMPLATE/3-iniciativa.yml)
- [✅ Tarea Growth](.github/ISSUE_TEMPLATE/4-tarea-growth.yml)
- [🐛 Bug Report](.github/ISSUE_TEMPLATE/5-bug-reporte.yml)
- [📝 Weekly Update](.github/ISSUE_TEMPLATE/6-weekly-update.yml)

## 🔄 Flujo de Trabajo

### Cadencia Semanal

| Día | Hora | Actividad | Responsable |
|-----|------|-----------|-------------|
| **Lunes** | 9:00am | OKR Review & Sprint Planning | Todo el equipo |
| **Miércoles** | 3:00pm | Metrics Check-in | Analytics Lead |
| **Viernes** | 4:00pm | Weekly Report & Retrospective | Growth Lead |

### Automatizaciones Activas

- ✅ **Sync diario de métricas** - 9:00am todos los días
- ✅ **Recordatorios semanales** - Lunes 8:30am
- ✅ **Reportes automáticos** - Viernes 5:00pm
- ✅ **Alertas de OKRs en riesgo** - Tiempo real

## 📊 Integraciones

| Herramienta | Estado | Frecuencia | Última Sync |
|-------------|--------|------------|-------------|
| Google Analytics 4 | ✅ Activo | Diario | Hoy 9:00am |
| Search Console | ✅ Activo | Semanal | Lunes |
| Supabase CRM | ✅ Activo | Diario | Hoy 9:00am |
| Slack | ✅ Activo | Tiempo real | Continuo |

## 👥 Equipo Growth

### Growth Squad
- **Growth Lead:** @yeison-gomez
- **SEO Lead:** @seo-lead
- **CRO Lead:** @cro-lead
- **Analytics Lead:** @analytics-lead
- **Content Lead:** @content-lead

### Responsabilidades por Área

| Área | Lead | Backup | OKRs Asignados |
|------|------|--------|----------------|
| SEO | @seo-lead | @content-lead | OBJ-1 |
| CRO | @cro-lead | @analytics-lead | OBJ-2 |
| Expansion | @growth-lead | @seo-lead | OBJ-3 |
| Analytics | @analytics-lead | @growth-lead | Soporte todos |

## 📈 Métricas Clave

### Tráfico (Google Analytics)
- **Sesiones mensuales:** 50,234 (-25% vs Q4 2024)
- **Usuarios únicos:** 38,421 (-22% vs Q4 2024)
- **Tasa de rebote:** 68% (+5pp vs Q4 2024)

### Conversión (CRM)
- **Tasa de conversión:** 1.2% (-0.3pp vs Q4 2024)
- **Ticket promedio:** $823 USD (-8% vs Q4 2024)
- **LTV:** $1,247 USD (-12% vs Q4 2024)

### SEO (Search Console)
- **Impresiones:** 234,521 (-18% vs Q4 2024)
- **CTR promedio:** 2.5% (-0.5pp vs Q4 2024)
- **Posición promedio:** 28.3 (+3.2 vs Q4 2024)

## 🛠️ Configuración

### Requisitos
- Python 3.8+
- GitHub CLI
- Acceso a Google Analytics 4
- Acceso a Search Console
- Credenciales Supabase

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/colombiatours/growth-system.git

# Instalar dependencias
pip install -r requirements.txt

# Configurar credenciales
cp .env.example .env
# Editar .env con tus credenciales

# Test de conexión
python scripts/test-connections.py
```

## 📚 Documentación

- [Guía del Equipo](docs/TEAM-GUIDE.md)
- [Metodología OKR](docs/OKR-METHODOLOGY.md)
- [Guía de Contribución](docs/CONTRIBUTING.md)
- [Playbook de Growth](okr-system/templates/growth-playbook.md)

## 🆘 Soporte

- **Slack:** #growth-team
- **Email:** growth@colombiatours.travel
- **Wiki:** [Growth Wiki](../../wiki)

## 📝 Changelog

### v1.0.0 (Enero 2025)
- ✅ Sistema inicial de OKRs
- ✅ Integración con Google Analytics
- ✅ Automatización de reportes
- ✅ Templates de issues

---

**Última actualización:** Enero 6, 2025 | **Próxima revisión OKR:** Abril 1, 2025