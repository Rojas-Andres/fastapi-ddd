
# 🌍 Map My World Backend

¡Bienvenido al backend de **Map My World**! Este proyecto implementa una API REST para explorar y revisar ubicaciones y categorías alrededor del mundo. La API permite gestionar ubicaciones, categorías y generar recomendaciones inteligentes para que las revisiones estén siempre frescas y relevantes.

## 🚀 ¿Qué es este proyecto?

Este proyecto es el corazón del sistema **Map My World**, una plataforma interactiva que permite a los usuarios descubrir lugares interesantes como restaurantes, parques y museos. Su principal objetivo es ofrecer recomendaciones actualizadas para mantener el contenido siempre relevante.

### ✨ Características principales:

- **Gestión de Ubicaciones y Categorías**: Añade y gestiona ubicaciones con coordenadas (latitud y longitud) y categorías específicas.
- **Recomendador de Exploración**: Genera combinaciones de ubicación-categoría que no han sido revisadas recientemente o que nunca se han revisado.
- **Control de Calidad**: Mantén un historial de revisiones para garantizar que todas las combinaciones se revisan periódicamente.

---

## 🛠️ Tecnologías utilizadas

Este proyecto utiliza un conjunto de herramientas modernas y eficientes para garantizar su rendimiento y escalabilidad:

- **Framework principal**: [FastAPI](https://fastapi.tiangolo.com/)
- **Base de datos**: PostgreSQL, gestionada mediante [SQLAlchemy](https://www.sqlalchemy.org/) y [Alembic](https://alembic.sqlalchemy.org/)
- **Pruebas y cobertura**: `pytest`, `pytest-mock`, `coverage`
- **Validación**: [Pydantic](https://docs.pydantic.dev/)
- **Entorno virtual**: `python-dotenv` para la gestión de configuraciones.
- **Servidor de desarrollo y producción**: `uvicorn` y `gunicorn`
- **Dependencias adicionales**: `httpx`, `Faker`, `pre-commit`, `psycopg2-binary`

---

## 📂 Estructura del proyecto

```
fastapi-challenge/
├── app/
│   ├── core/                 # Configuración central y middleware
│   │   ├── config.py         # Configuración de la aplicación
│   │   ├── exceptions.py     # Manejo centralizado de excepciones
│   │   └── middleware.py     # Definición de middlewares personalizados
│   │
│   ├── infraestructure/      # Infraestructura de la aplicación
│   │   ├── api/              # Definición de rutas y controladores de la API
│   │   └── database/         # Configuración y gestión de la base de datos
│   │
│   ├── modules/
│   │   ├── category/
│   │   ├── reviews/
│   │   ├── location/
│   │   └── shared/
│   │
│   ├── main.py               # Punto de entrada principal de la aplicación
│   └── gunicorn.conf.py      # Configuración para el servidor Gunicorn
│
├── tests/                    # Pruebas unitarias y de integración
├── alembic/                  # Migraciones de la base de datos
├── configuration/            # Archivos relacionados con configuraciones generales
├── images/                   # Recursos de imágenes utilizados en la documentación
├── nginx/                    # Configuración para el servidor Nginx
├── requirements/             # Dependencias del proyecto divididas por entorno
├── scripts_docker/           # Scripts personalizados para la gestión con Docker
├── .code_quality/            # Configuración para herramientas de análisis de código
├── .vs_code/                 # Configuración para el entorno de desarrollo en VS Code
├── .github/workflows         # Definiciones para los flujos de trabajo de GitHub Actions
├── .env.example              # Configuración del entorno (plantilla)
└── README.md                 # Documentación del proyecto

```

---

## 🚀 ¿Cómo lo utilizo?

### 1. **Requisitos previos**

- Python 3.10 o superior.
- PostgreSQL instalado y configurado.
- `pip` para instalar dependencias.

### 2. **Instalación**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/map-my-world.git
   cd map-my-world/backend
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements/local.txt
   ```

3. Configura las variables de entorno en un archivo `.env` basado en `.env.example`.

4. Aplica las migraciones a la base de datos:
   ```bash
   alembic upgrade head
   ```

### 3. **Ejecutar el proyecto**

- Para desarrollo:
  ```bash
  uvicorn app.main:app --reload
  ```

- Para producción:
  ```bash
  gunicorn -k uvicorn.workers.UvicornWorker app.main:app
  ```

### 4. **Documentación interactiva**

Accede a la documentación de la API en:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Pruebas

Ejecuta las pruebas con:
```bash
pytest .
```

---

## ⚙️ Correr proyecto con Docker

1. Asegúrate de haber configurado el archivo `.env` en la raíz del proyecto.

2. Construye las imágenes de Docker:
   ```bash
   docker-compose build
   ```

3. Inicia los contenedores:
   ```bash
   docker-compose up
   ```

---


## 🔄 Github CICD Validaciones

### Total de test ejecutados
![](images/github_actions/test_success.png)

### Validación de pre-commit
![](images/github_actions/github_action_pre_commit_and_coverge_pass.png)

---

## 📖 Documentación adicional

### Swagger
![](images/docs/swagger_doc.png)

### Diagrama ER
![](images/diagrama/diagrama_er.png)

---

## 🌐 Despliegue AWS

### Creación de parámetros en Secrets Manager para CloudFormation
![](images/deployment/creation_params_store.png)

### Bucket para guardar las variables de entorno
![](images/deployment/bucket_save_envs.png)

### Creación de ECR para imágenes Docker
![](images/deployment/creation_images_ecr.png)

### Ejecución exitosa de CodePipeline
![](images/deployment/codepipeline_success.png)

### Load Balancer activo
![](images/deployment/aplication_load_balancer_active.png)

### Tarea ECS Fargate ejecutada exitosamente
![](images/deployment/tarea_ecs_execute.png)

### Logs de ECS Fargate
![](images/deployment/logs_task_ecs.png)

### CloudFormation ejecutado exitosamente
![](images/deployment/cloudformation_success.png)

### Acceso al Load Balancer en el puerto 8000
![](images/deployment/access_8000_load_balancer.png)

---

# Por motivos de costos se eliminaron los bucket y el stack. Se deja en evidencia que el proyecto se puede desplegar en AWS en ECS con fargate

## 📝 Notas finales

Por motivos de costos, los buckets y el stack fueron eliminados, pero este proyecto demuestra cómo puede desplegarse en AWS utilizando ECS con Fargate.

**Referencias:**
- [Unidad de Trabajo - Cosmic Python](https://www.cosmicpython.com/book/chapter_06_uow.html)
- [Repositorio original de referencia](https://github.com/cosmicpython/code.git)


## ✍️ Creado por Andrés Rojas

**Repositorio GitHub:** [fastapi-challenge](https://github.com/Rojas-Andres/fastapi-challenge)