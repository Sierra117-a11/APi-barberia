# El Arte del Barbero - Plataforma Web con Backend

### ✨ Plataforma web integrada con API para una barbería moderna

![GitHub last commit](https://img.shields.io/github/last-commit/Sierra117-a11/APi-barberia)

## ✨ Descripción
El Arte del Barbero es una plataforma completa que incluye tanto frontend como backend. Permite agendar citas, explorar estilos de cortes, conocer al equipo, y contactar fácilmente a la barbería, todo desde una interfaz moderna y responsiva.

## 🌐 Tecnologías utilizadas
- **HTML5** y **CSS3** para la estructura y diseño del sitio.
- **JavaScript** para la lógica del cliente.
- **Python (FastAPI)** para el backend y manejo de rutas.
- **Pydantic** para validación de datos.
- **SQLite** o similar para almacenamiento de datos.
- **Git** para control de versiones.

## 📖 Estructura del proyecto
- `index.html` – Página principal.
- `quienes-somos.html` – Sección sobre la barbería.
- `cortes-y-estilos.html` – Galería de cortes y estilos.
- `agendarcita.html` – Página para agendar citas.
- `estilos.css` – Estilos globales.
- `scripts.js` – Lógica del cliente (JS).
- `main.py` – Punto de entrada del backend con FastAPI.
- `conection.py` – Conexión a base de datos.
- `controllers/`, `routes/`, `models/`, `schemas/` – Arquitectura del backend.

## ⚖️ Características principales
- **Interfaz responsiva** con navegación clara.
- **Sistema de citas** conectado a un backend.
- **Arquitectura backend organizada** en controladores, modelos y rutas.
- **Validación de datos** con Pydantic.

## 🔧 Instalación y uso

1. **Clonar el repositorio**
   ```bash
  git clone https://github.com/Sierra117-a11/APi-barberia.git
  cd APi-barberia-master
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el servidor**
   ```bash
   uvicorn main:app --reload
   ```

4. **Abrir el frontend**
   - Abre `index.html` en tu navegador para explorar el sitio.

5. **Probar el API**
   - Visita `http://127.0.0.1:8000/docs` para acceder a la documentación automática de la API con Swagger.

## 💬 Contacto
¿Tienes preguntas o sugerencias? Contáctanos:

- **Email:** contacto@barberiavicger.com
- **Instagram:** [@barberiavicger](https://instagram.com/barberiavicger)

## 👨‍🎨 Diseñadores
- Victor Yepes  
- Jose Camargo  
- Julián Venegas  
- Germán Gutiérrez

---
*© 2025 El Arte del Barbero. Todos los derechos reservados.*
