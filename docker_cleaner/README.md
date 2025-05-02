# 🐳 Docker Cleaner

Una herramienta interactiva y versátil para limpiar tu entorno Docker de forma segura, visual y extensible.  
Diseñada con amor (y logs) para DevOps como tú que odian perder tiempo en tareas repetitivas.

---

## 🎯 Objetivo

Automatizar, revisar y ejecutar limpiezas de recursos Docker (contenedores, imágenes, volúmenes, redes) con distintas interfaces, permitiendo elegir entre consola, terminal TUI, GUI web o contenedor Docker.

---

## 🧰 Finalidad

- Liberar espacio automáticamente de recursos no utilizados.
- Visualizar el estado actual de Docker.
- Ejecutar comandos con validaciones y logs.
- Elegir cómo quieres interactuar: CLI, TUI, Web o Docker.

---

## 🗂️ Estructura del Proyecto

docker_cleaner/
├── app/
│ ├── init.py
│ ├── cleaner.py # Lógica principal de limpieza Docker
│ ├── cli.py # Menú en consola con Rich
│ ├── tui.py # Interfaz de texto con Textual
│ ├── web.py # API REST con Flask
│ └── utils.py # Utilidades: validaciones, logs
├── Dockerfile # Imagen Docker ejecutable
├── requirements.txt # Dependencias del proyecto
├── docker_cleaner.log # Logs de ejecución (autogenerado)
└── README.md # Este archivo


---

## 🧪 Modo CLI (Consola clásica con Rich)

```bash
python -m app.cli
```
Permite navegar por un menú de texto en la consola, usando teclas numéricas. Ideal para uso rápido desde terminales SSH o shell scripts.

🎛️ Modo TUI (Interfaz de texto interactiva)

```bash
python -m app.tui
```
Abre una interfaz estilo terminal con botones interactivos. Ideal para quienes disfrutan el modo visual sin salir del terminal.

🖥️ Modo Web (API REST con Flask)

```bash
python -m app.web
```

Endpoints disponibles:

GET /status → Estado de contenedores, imágenes y volúmenes

GET /clean/basic → Limpieza básica

GET /clean/advanced → Limpieza avanzada (-a)

GET /clean/volumes → Limpieza de volúmenes

GET /disk → Uso de disco

Luego accede desde tu navegador a:
📡 http://localhost:5000/status

🐳 Ejecutar en Docker

1. Construir imagen
```bash
docker build -t docker-cleaner .
```
2. Ejecutar con acceso al Docker del host
```bash
docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock docker-cleaner
```
✅ Por defecto se ejecuta el modo CLI.
Puedes cambiarlo modificando CMD en el Dockerfile.

📝 Logs
Todos los comandos ejecutados y errores quedan registrados en:
```bash
docker_cleaner.log
```

📊 Diagrama del flujo de ejecución

                ┌────────────────────────────┐
                │        Interfaz CLI        │
                ├────────────┬───────────────┤
                │            │               │
         TUI (textual)    Flask API       Docker CLI
                │            │               │
                └──────┬─────┴────┬──────────┘
                       │          │
               ┌───────▼──────────▼─────────┐
               │      Módulo cleaner.py     │
               │ Ejecuta comandos Docker +  │
               │ registra logs en .log file │
               └────────────┬───────────────┘
                            │
                     Subprocess + Logs

✍️ Autor
Jaime A. Henao A.
DevOps / Cloud Engineer ☁️ 🛠️
📧 Contacto disponible bajo solicitud

💡 Próximas mejoras
Configuración por archivo .env

Autenticación básica para API web

Programador de tareas (cron-style)

GUI desktop con Tkinter o Electron

¡Gracias por usar Docker Cleaner!
💥 Haz que tu entorno Docker vuelva a respirar.

