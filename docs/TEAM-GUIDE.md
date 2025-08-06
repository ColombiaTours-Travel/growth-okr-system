# 📚 Guía del Equipo Growth - Colombiatours

## 🎯 Nuestra Misión

Posicionar a Colombiatours.travel como el líder indiscutible del turismo receptivo internacional en Colombia, triplicando nuestro crecimiento y dominando los mercados clave de México, España y USA.

## 🚀 Sistema de Gestión OKR con GitHub Projects

### ¿Por qué GitHub Projects?

- **Centralización:** Todo en un solo lugar - código, métricas, tareas
- **Transparencia:** Visibilidad total del progreso para todo el equipo
- **Automatización:** Métricas actualizadas automáticamente desde GA4, GSC y CRM
- **Costo:** $0 - Ya incluido en nuestro plan GitHub
- **Integración:** Conectado con nuestro flujo de desarrollo

## 📋 Cómo Usar el Sistema

### 1. Estructura de Proyectos

Tenemos 3 proyectos principales en GitHub:

#### 📊 [Growth OKRs 2025](https://github.com/orgs/ColombiaTours-Travel/projects/1)
- **Qué:** Objetivos y Key Results trimestrales
- **Quién:** Todo el equipo revisa, owners actualizan
- **Cuándo:** Review semanal los lunes

#### 👥 [Growth Team Management](https://github.com/orgs/ColombiaTours-Travel/projects/2)
- **Qué:** Gestión de capacidad y asignaciones
- **Quién:** Growth Lead y Team Leads
- **Cuándo:** Planning quincenal

#### 🎯 [Growth Initiatives](https://github.com/orgs/ColombiaTours-Travel/projects/3)
- **Qué:** Tareas e iniciativas diarias
- **Quién:** Todo el equipo
- **Cuándo:** Daily standup

### 2. Flujo de Trabajo Semanal

#### 🗓️ Lunes - OKR Review & Planning
**9:00 AM - 10:00 AM**

1. Revisar progreso de OKRs en el dashboard
2. Identificar blockers y riesgos
3. Planificar sprint de la semana
4. Asignar iniciativas prioritarias

**Cómo participar:**
- Abre el [proyecto OKRs](https://github.com/orgs/ColombiaTours-Travel/projects/1)
- Revisa la vista "Weekly Status"
- Actualiza tus KRs asignados
- Comenta en issues con blockers

#### 🗓️ Miércoles - Metrics Check-in
**3:00 PM - 3:30 PM**

1. Revisar métricas actualizadas automáticamente
2. Analizar tendencias y alertas
3. Ajustar tácticas si es necesario

#### 🗓️ Viernes - Weekly Report
**4:00 PM - 5:00 PM**

1. Completar weekly update en el issue generado
2. Documentar wins y learnings
3. Preparar prioridades para siguiente semana

### 3. Crear y Gestionar Issues

#### Para crear un nuevo OKR:
```bash
# Desde GitHub UI
1. Ve a Issues → New Issue
2. Selecciona "🎯 OKR - Objetivo Trimestral"
3. Completa el formulario
4. Asigna al proyecto "Growth OKRs 2025"

# Desde CLI
gh issue create --template okr-objetivo.yml
```

#### Para crear un Key Result:
```bash
# Vincula siempre a un objetivo existente
1. New Issue → "📊 Key Result"
2. Referencia el objetivo con #[número]
3. Define métricas claras y medibles
```

#### Para crear una Iniciativa:
```bash
# Vincula a un KR específico
1. New Issue → "💡 Iniciativa Growth"
2. Estima esfuerzo (XS/S/M/L/XL)
3. Define plan de acción claro
```

### 4. Vistas del Proyecto

#### Vista OKR Dashboard
- **Uso:** Visión general del trimestre
- **Filtros:** Por objetivo, por owner, por estado
- **Actualización:** Automática diaria

#### Vista Team Workload
- **Uso:** Ver carga de trabajo del equipo
- **Agrupado por:** Persona
- **Ordenado por:** Prioridad

#### Vista Roadmap
- **Uso:** Timeline de iniciativas
- **Período:** Trimestral
- **Agrupado por:** Área (SEO, CRO, etc)

### 5. Automatizaciones Activas

#### 🤖 Sync Diario de Métricas (9:00 AM)
- Google Analytics → Issues de KRs
- Search Console → Métricas SEO
- CRM → Revenue y conversiones

#### 📊 Reportes Automáticos (Viernes 5:00 PM)
- Genera resumen semanal
- Envía a Slack #growth-team
- Actualiza dashboards

#### 🚨 Alertas en Tiempo Real
- OKRs en riesgo (progress < expected)
- Métricas cayendo >10%
- Deadlines próximos

## 📏 Metodología OKR

### Principios Clave

1. **Objetivos Inspiradores:** Ambiciosos pero alcanzables
2. **Key Results Medibles:** Números específicos, no actividades
3. **Transparencia Total:** Todo visible para el equipo
4. **Actualización Continua:** Métricas en tiempo real
5. **Foco Trimestral:** 3-5 objetivos máximo

### Cómo Escribir Buenos OKRs

#### ✅ Objetivo Efectivo:
"Dominar el tráfico orgánico internacional posicionando a Colombiatours como líder en turismo receptivo"

#### ❌ Objetivo Pobre:
"Mejorar SEO"

#### ✅ Key Result Efectivo:
"Aumentar tráfico orgánico internacional de 50K a 75K sesiones/mes"

#### ❌ Key Result Pobre:
"Publicar más contenido"

### Scoring de OKRs

- **0.0 - 0.3:** 🔴 Fallo (necesita revisión urgente)
- **0.4 - 0.6:** 🟡 Progreso (necesita aceleración)
- **0.7 - 0.9:** 🟢 Éxito (bien encaminado)
- **1.0:** 🎯 Excepcional (superado)

## 🛠️ Herramientas y Accesos

### Necesitas acceso a:

1. **GitHub Projects**
   - Solicita acceso al org: ColombiaTours-Travel
   - Permisos: Write en los 3 proyectos

2. **Google Analytics 4**
   - Property: colombiatours.travel
   - Vista: Growth Team Dashboard

3. **Search Console**
   - Propiedad: https://colombiatours.travel
   - Permisos: Full

4. **Supabase CRM**
   - Project: colombiatours-prod
   - Role: analyst

5. **Slack**
   - Canal: #growth-team
   - Alertas: Activadas

### Configuración Local

```bash
# 1. Clonar repositorio
git clone https://github.com/ColombiaTours-Travel/growth-system.git
cd growth-system

# 2. Instalar GitHub CLI
brew install gh  # Mac
# o
sudo apt install gh  # Linux

# 3. Autenticarse
gh auth login

# 4. Configurar Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Configurar credenciales
cp .env.example .env
# Editar .env con tus credenciales

# 6. Test
python scripts/test-connections.py
```

## 📊 KPIs y Métricas Clave

### Métricas Primarias (OKR)

| Métrica | Fuente | Frecuencia | Owner |
|---------|--------|------------|-------|
| Tráfico Orgánico Internacional | GA4 | Diario | @seo-lead |
| Tasa de Conversión | GA4 + CRM | Diario | @cro-lead |
| Abandono de Carrito | GA4 | Semanal | @cro-lead |
| Revenue por País | CRM | Diario | @growth-lead |
| Ticket Promedio | CRM | Semanal | @analytics-lead |

### Métricas de Soporte

- CTR orgánico (Search Console)
- Posiciones keywords (Search Console)
- Page Speed (PageSpeed Insights)
- Core Web Vitals (Search Console)
- Engagement Rate (GA4)
- LTV/CAC (CRM + Ads)

## 🎯 Roles y Responsabilidades

### Growth Lead (@yeison-gomez)
- Owner de objetivos generales
- Facilitar OKR reviews
- Reportes a leadership
- Gestión de recursos

### SEO Lead
- Owner Objetivo 1 (Tráfico Orgánico)
- Estrategia de contenido
- Link building
- Technical SEO

### CRO Lead
- Owner Objetivo 2 (Conversión)
- A/B testing
- UX optimization
- Funnel analysis

### Analytics Lead
- Mantenimiento dashboards
- Análisis de datos
- Reportes automáticos
- Tracking implementation

### Content Lead
- Producción de contenido
- Localización
- SEO copywriting
- Email marketing

## 🚨 Proceso de Escalación

### Nivel 1: Blocker Operativo
→ Comentar en issue
→ Mencionar a owner
→ Resolver en daily standup

### Nivel 2: Riesgo para KR
→ Cambiar estado a 🟡 At Risk
→ Documentar en issue
→ Escalar en weekly review

### Nivel 3: Riesgo para Objetivo
→ Cambiar estado a 🔴 Off Track
→ Notificar a Growth Lead inmediatamente
→ Crear plan de mitigación

## 📚 Recursos Adicionales

### Documentación
- [Metodología OKR](OKR-METHODOLOGY.md)
- [Playbook de Growth](../okr-system/templates/growth-playbook.md)
- [GitHub Projects Guide](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

### Templates
- [OKR Planning Template](../okr-system/templates/okr-template.md)
- [Weekly Report Template](../okr-system/templates/weekly-report.md)
- [Sprint Planning Template](../okr-system/templates/sprint-planning.md)

### Herramientas Externas
- [Google Analytics](https://analytics.google.com)
- [Search Console](https://search.google.com/search-console)
- [Supabase Dashboard](https://app.supabase.io)
- [Ahrefs](https://ahrefs.com) - SEO Research

## ❓ FAQ

**P: ¿Cómo actualizo el progreso de un KR?**
R: El progreso se actualiza automáticamente desde las fuentes de datos. Para actualización manual, edita el issue y actualiza el campo "Progress" en el proyecto.

**P: ¿Dónde veo el dashboard completo?**
R: En GitHub Projects → Growth OKRs 2025 → Vista "OKR Dashboard"

**P: ¿Cómo reporto un blocker?**
R: Comenta en el issue relacionado con el tag @growth-lead y cambia el estado a "🟡 At Risk"

**P: ¿Cuándo se actualizan las métricas?**
R: Automáticamente todos los días a las 9:00 AM Colombia time

**P: ¿Cómo propongo un nuevo OKR?**
R: Crea un draft usando el template y preséntalo en el planning trimestral

## 🆘 Soporte

- **Slack:** #growth-team
- **Email:** growth@colombiatours.travel
- **GitHub Issues:** Para problemas técnicos
- **Growth Lead:** @yeison-gomez

---

**Última actualización:** Enero 6, 2025  
**Próxima revisión:** Febrero 1, 2025