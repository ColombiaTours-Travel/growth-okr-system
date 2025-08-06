#!/bin/bash

# Script para configurar los proyectos de GitHub con campos personalizados y vistas
# Colombiatours Growth Team - OKR System Setup

echo "🚀 Configurando proyectos de GitHub para el sistema OKR..."

# IDs de los proyectos
PROJECT_OKR_ID="PVT_kwDODWf2Fc4A_wzb"  # Growth OKRs 2025
PROJECT_TEAM_ID="PVT_kwDODWf2Fc4A_wzd"  # Growth Team Management
PROJECT_INIT_ID="PVT_kwDODWf2Fc4A_wzf"  # Growth Initiatives Q1 2025

# Función para crear campos personalizados
create_custom_fields() {
    local PROJECT_ID=$1
    local PROJECT_NAME=$2
    
    echo "📊 Configurando campos para: $PROJECT_NAME"
    
    # Campo: Progress (0-100%)
    echo "  - Creando campo Progress..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: NUMBER
        name: \"Progress\"
      }) {
        projectV2Field {
          ... on ProjectV2Field {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Progress ya existe o error"
    
    # Campo: Status
    echo "  - Creando campo Status..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: SINGLE_SELECT
        name: \"Status\"
        singleSelectOptions: [
          {name: \"🟢 On Track\", color: GREEN}
          {name: \"🟡 At Risk\", color: YELLOW}
          {name: \"🔴 Off Track\", color: RED}
          {name: \"⚪ Not Started\", color: GRAY}
        ]
      }) {
        projectV2Field {
          ... on ProjectV2SingleSelectField {
            id
            name
            options {
              name
            }
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Status ya existe o error"
    
    # Campo: Quarter
    echo "  - Creando campo Quarter..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: SINGLE_SELECT
        name: \"Quarter\"
        singleSelectOptions: [
          {name: \"Q1 2025\", color: BLUE}
          {name: \"Q2 2025\", color: GREEN}
          {name: \"Q3 2025\", color: YELLOW}
          {name: \"Q4 2025\", color: RED}
        ]
      }) {
        projectV2Field {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Quarter ya existe o error"
    
    # Campo: Area
    echo "  - Creando campo Area..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: SINGLE_SELECT
        name: \"Area\"
        singleSelectOptions: [
          {name: \"SEO\", color: GREEN}
          {name: \"CRO\", color: BLUE}
          {name: \"Analytics\", color: PURPLE}
          {name: \"Content\", color: YELLOW}
          {name: \"Paid Media\", color: ORANGE}
          {name: \"Email\", color: PINK}
        ]
      }) {
        projectV2Field {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Area ya existe o error"
    
    # Campo: Priority
    echo "  - Creando campo Priority..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: SINGLE_SELECT
        name: \"Priority\"
        singleSelectOptions: [
          {name: \"P0 - Critical\", color: RED}
          {name: \"P1 - High\", color: ORANGE}
          {name: \"P2 - Medium\", color: YELLOW}
          {name: \"P3 - Low\", color: GREEN}
        ]
      }) {
        projectV2Field {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Priority ya existe o error"
    
    # Campo: Target (para métricas)
    echo "  - Creando campo Target..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: NUMBER
        name: \"Target\"
      }) {
        projectV2Field {
          ... on ProjectV2Field {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Target ya existe o error"
    
    # Campo: Current (para métricas actuales)
    echo "  - Creando campo Current..."
    gh api graphql -f query="
    mutation {
      createProjectV2Field(input: {
        projectId: \"$PROJECT_ID\"
        dataType: NUMBER
        name: \"Current\"
      }) {
        projectV2Field {
          ... on ProjectV2Field {
            id
            name
          }
        }
      }
    }" 2>/dev/null || echo "    Campo Current ya existe o error"
    
    # Campo: Sprint (para iniciativas)
    if [ "$PROJECT_NAME" == "Growth Initiatives Q1 2025" ]; then
        echo "  - Creando campo Sprint..."
        gh api graphql -f query="
        mutation {
          createProjectV2Field(input: {
            projectId: \"$PROJECT_ID\"
            dataType: ITERATION
            name: \"Sprint\"
          }) {
            projectV2Field {
              ... on ProjectV2IterationField {
                id
                name
              }
            }
          }
        }" 2>/dev/null || echo "    Campo Sprint ya existe o error"
    fi
    
    echo "  ✅ Campos configurados para $PROJECT_NAME"
}

# Función para agregar issues a proyectos
add_issues_to_project() {
    local PROJECT_ID=$1
    local PROJECT_NAME=$2
    
    echo "📎 Agregando issues a: $PROJECT_NAME"
    
    # Obtener issues del repositorio
    ISSUE_IDS=$(gh api repos/ColombiaTours-Travel/growth-okr-system/issues --jq '.[].node_id')
    
    for ISSUE_ID in $ISSUE_IDS; do
        echo "  - Agregando issue $ISSUE_ID..."
        gh api graphql -f query="
        mutation {
          addProjectV2ItemById(input: {
            projectId: \"$PROJECT_ID\"
            contentId: \"$ISSUE_ID\"
          }) {
            item {
              id
            }
          }
        }" 2>/dev/null || echo "    Issue ya agregado o error"
    done
    
    echo "  ✅ Issues agregados a $PROJECT_NAME"
}

# Función para crear vistas
create_project_views() {
    local PROJECT_ID=$1
    local PROJECT_NAME=$2
    
    echo "👁️ Configurando vistas para: $PROJECT_NAME"
    
    # Nota: Las vistas se deben crear manualmente en la UI de GitHub
    # Aquí documentamos las vistas recomendadas
    
    cat << EOF

  📌 Vistas recomendadas para configurar manualmente en $PROJECT_NAME:
  
  1. **OKR Dashboard** (Vista Board/Kanban)
     - Agrupar por: Status
     - Columnas: Not Started → On Track → At Risk → Off Track
     - Filtros: Quarter = Q1 2025
  
  2. **Timeline View** (Vista Roadmap)
     - Fecha inicio: Campo personalizado Start Date
     - Fecha fin: Campo personalizado End Date
     - Agrupar por: Area
  
  3. **Metrics Table** (Vista Tabla)
     - Columnas: Title, Progress, Current, Target, Status, Owner
     - Ordenar por: Priority (descendente)
     - Filtros: Labels contiene "key-result"
  
  4. **Team Workload** (Vista Tabla)
     - Agrupar por: Assignee
     - Columnas: Title, Status, Priority, Progress
     - Ordenar por: Priority
  
  Para crear estas vistas:
  1. Ve a https://github.com/orgs/ColombiaTours-Travel/projects/${PROJECT_ID#*_}
  2. Click en "New view"
  3. Configura según las especificaciones anteriores
  
EOF
}

# Ejecutar configuración para cada proyecto
echo "========================================="
echo "1️⃣ Configurando: Growth OKRs 2025"
echo "========================================="
create_custom_fields "$PROJECT_OKR_ID" "Growth OKRs 2025"
add_issues_to_project "$PROJECT_OKR_ID" "Growth OKRs 2025"
create_project_views "$PROJECT_OKR_ID" "Growth OKRs 2025"

echo ""
echo "========================================="
echo "2️⃣ Configurando: Growth Team Management"
echo "========================================="
create_custom_fields "$PROJECT_TEAM_ID" "Growth Team Management"
create_project_views "$PROJECT_TEAM_ID" "Growth Team Management"

echo ""
echo "========================================="
echo "3️⃣ Configurando: Growth Initiatives Q1 2025"
echo "========================================="
create_custom_fields "$PROJECT_INIT_ID" "Growth Initiatives Q1 2025"
add_issues_to_project "$PROJECT_INIT_ID" "Growth Initiatives Q1 2025"
create_project_views "$PROJECT_INIT_ID" "Growth Initiatives Q1 2025"

echo ""
echo "========================================="
echo "✅ CONFIGURACIÓN COMPLETADA"
echo "========================================="
echo ""
echo "📋 Próximos pasos:"
echo "1. Revisa los proyectos en:"
echo "   - https://github.com/orgs/ColombiaTours-Travel/projects/1 (OKRs)"
echo "   - https://github.com/orgs/ColombiaTours-Travel/projects/2 (Team)"
echo "   - https://github.com/orgs/ColombiaTours-Travel/projects/3 (Initiatives)"
echo ""
echo "2. Configura manualmente las vistas según las recomendaciones"
echo "3. Ajusta los valores de los campos personalizados en cada issue"
echo "4. Invita a los miembros del equipo a los proyectos"
echo ""
echo "🚀 El sistema OKR está listo para usar!"