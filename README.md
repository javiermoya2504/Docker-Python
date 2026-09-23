# Students App

Aplicación de ejemplo construida con FastAPI, SQLAlchemy y PostgreSQL, pensada para
enseñar el flujo completo: primero el entorno local, después Docker.

## 1. Entorno local (sin Docker)

Este paso no requiere tener una base de datos levantada. La app arranca igual y,
si no encuentra la base de datos, la página de alumnos se muestra vacía en vez
de dar un error.

### Crear y activar el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Configurar las variables de entorno

```bash
cp .env.example .env
```

Puedes revisar y ajustar el valor de `DATABASE_URL` en `.env` si lo necesitas.

### Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

Abre [http://localhost:8000](http://localhost:8000). Verás "No hay alumnos
registrados." porque todavía no hay ninguna base de datos disponible — y no
un error 500, que es justo el comportamiento esperado en este punto.

> **Nota:** el comando de arranque siempre es `uvicorn app.main:app`, nunca
> `python app/main.py`. FastAPI necesita un servidor ASGI (Uvicorn) para
> ejecutarse, no se lanza como un script plano.

## 2. Con Docker (base de datos incluida)

Una vez entendido el paso anterior, se levanta todo el stack (app + PostgreSQL)
con Docker Compose:

```bash
docker compose up --build
```

Esto crea el contenedor de PostgreSQL, carga los datos iniciales de
[`database_students.sql`](database_students.sql) y arranca la app conectada a
esa base de datos. Ahora en [http://localhost:8000](http://localhost:8000) sí
se verá el listado de alumnos.

Para detener y eliminar los contenedores:

```bash
docker compose down
```

## Estructura del proyecto

```
app/
  main.py        # Rutas de FastAPI
  database.py     # Conexión y sesión de SQLAlchemy
  models.py       # Modelos ORM
templates/         # Vistas Jinja2 (Bootstrap)
database_students.sql   # Datos iniciales para PostgreSQL
```
