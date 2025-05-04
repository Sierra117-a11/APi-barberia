# El Arte del Barbero - Plataforma Web con Backend

### ✨ Plataforma web integrada con API para una barbería moderna

![GitHub last commit](https://img.shields.io/github/last-commit/Sierra117-a11/APi-barberia)

## ✨ Descripción
El Arte del Barbero es una plataforma completa que incluye tanto frontend como backend. Permite agendar citas, explorar estilos de cortes, conocer al equipo, y contactar fácilmente a la barbería, todo desde una interfaz moderna y responsiva.

Este proyecto es una aplicación web para la gestión de una barbería, desarrollada con un enfoque fullstack. 
Permite a los usuarios **registrarse, iniciar sesión y agendar citas**, mientras que los administradores 
pueden gestionar información relacionada con los servicios ofrecidos.

---

## 🚀 Tecnologías utilizadas

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: FastAPI (Python)
- **Base de datos**: SQLite
- **Servidor local**: Uvicorn

---

# Estructura del Proyecto - API-barberia

Este repositorio contiene una aplicación completa para una barbería, con frontend y backend integrados.

## Estructura de Carpetas

API-barberia/
│
├── backend/ # Lógica del servidor (API)
│ ├── app.py # Archivo principal de la aplicación
│ ├── config/ # Configuración de la base de datos y variables de entorno
│ ├── models/ # Definición de modelos de datos (ORM)
│ ├── controllers/ # Lógica de controladores (CRUD)
│ ├── routes/ # Definición de rutas de la API
│ ├── scripts/ # Scripts SQL para inicializar/configurar la base de datos
│ └── requirements.txt # Lista de dependencias del proyecto
│
└── frontend/ # Interfaz de usuario
├── index.html # Página principal
├── quienes-somos.html # Sección sobre la barbería
├── cortes-y-estilos.html # Galería de cortes y estilos
├── agendar.html # Página para agendar citas
├── configurar-usuario.html # Página para gestionar datos del usuario
├── contactos.html # Página de contacto o comentarios
├── estilos.css # Estilos globales (CSS)
└── scripts.js # Lógica del cliente (JavaScript)

---

## ⚙️ Instalación y ejecución local

1. **Clona el repositorio:**

```bash
git clone https://github.com/Sierra117-a11/APi-barberia.git
cd APi-barberia
Instala las dependencias del backend (requiere Python 3.10+):

bash

pip install fastapi uvicorn
Ejecuta el servidor FastAPI:

bash

cd backend
uvicorn main:app --reload

Abre el frontend:

Abre el archivo index.html en el navegador desde la carpeta frontend o configura un servidor local si deseas simular rutas más realistas.

👤 Manual de usuario
1. Ingreso a la plataforma
Al abrir el sitio, lo primero que verás es la pantalla de inicio de sesión (login.html). Debes ingresar con tu correo y contraseña registrados.

Si aún no tienes cuenta, puedes ir a la opción de registro.

Sin iniciar sesión, las opciones están limitadas (No podras visualizar otras funciones).

2. Funcionalidades disponibles luego de iniciar sesión:

Agendar cita: Acceso al formulario para seleccionar fecha, hora y tipo de corte.

configuración de usuario: podrás ver , actualizar y eliminar tu usuario 

Los enlaces del menú aparecerán únicamente después del inicio de sesión exitoso.

🛡 Seguridad
Este proyecto ha sido simplificado y no utiliza JWT ni tokens de autenticación. Toda la lógica de sesión es mínima, pensada para pruebas locales o desarrollo básico.

📌 Notas adicionales
Este proyecto está en desarrollo y puede ser extendido con funcionalidades como panel de administrador, historial de citas, recordatorios por correo, etc.

Ideal para aprendizaje o implementación de prototipos rápidos de sistemas de agenda web.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Puedes clonar el proyecto, crear una nueva rama y proponer mejoras mediante pull requests.

📫 Contacto
Proyecto creado por Jose Camargo, Julian Venegas, German Gutierrez y Victor Yepez
## 👨‍🎨 Diseñadores
- Victor Yepes  
- Jose Camargo  
- Julián Venegas  
- Germán Gutiérrez

---
*© 2025 El Arte del Barbero. Todos los derechos reservados.*
