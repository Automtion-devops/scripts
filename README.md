# 🐳 Docker Cleaner

Una herramienta interactiva, modular y extensible para mantener tu entorno Docker limpio y eficiente. Perfecta para DevOps que valoran el orden... y el tiempo.

---

## 📚 Índice

1. [🎯 Objetivo](#-objetivo)
2. [🧰 Finalidad](#-finalidad)
3. [🗂️ Estructura del Proyecto](#️-estructura-del-proyecto)
4. [🧪 Modo CLI](#-modo-cli)
5. [🎛️ Modo TUI](#-modo-tui)
6. [🖥️ Modo Web](#-modo-web)
7. [🐳 Ejecutar en Docker](#-ejecutar-en-docker)
8. [📝 Logs](#-logs)
9. [📊 Diagrama del flujo de ejecución](#-diagrama-del-flujo-de-ejecución)
10. [🔐 Configuración SSH para múltiples cuentas GitHub](#-configuración-ssh-para-múltiples-cuentas-github)
11. [✍️ Autor](#-autor)
12. [💡 Próximas mejoras](#-próximas-mejoras)

---

## 🎯 Objetivo

Automatizar y centralizar la limpieza de contenedores, imágenes, redes y volúmenes de Docker, con una experiencia de usuario multiplataforma: CLI, TUI, Web o contenedor.

---

## 🧰 Finalidad

- Ahorrar tiempo limpiando recursos inactivos.
- Visualizar el estado de Docker fácilmente.
- Facilitar su ejecución desde distintos entornos (terminal, navegador o Docker).

---

## 🗂️ Estructura del Proyecto

```plaintext
docker_cleaner/
├── app/
│   ├── __init__.py
│   ├── cleaner.py        # Lógica principal de limpieza Docker
│   ├── cli.py            # Menú en consola con Rich
│   ├── tui.py            # Interfaz de texto con Textual
│   ├── web.py            # API REST con Flask
│   ├── utils.py          # Utilidades: validaciones, logs
│   ├── static/           # Archivos estáticos (CSS, JS)
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── templates/        # Plantillas HTML
│   │   └── index.html
├── Dockerfile            # Imagen Docker ejecutable
├── requirements.txt      # Dependencias del proyecto
├── docker_cleaner.log    # Logs de ejecución (autogenerado)
└── [README.md](http://_vscodecontentref_/1)             # Este archivo
```

---

## 🧪 Modo CLI

Ejecuta el siguiente comando para iniciar el menú interactivo en la consola:

```bash
python -m app.cli
```

Permite navegar por un menú de texto en la consola, usando teclas numéricas. Ideal para uso rápido desde terminales SSH o shell scripts.

* Características:
- Navega por un menú de texto usando teclas numéricas.
- Ideal para uso rápido desde terminales SSH o scripts.

---

## 🎛️ Modo TUI

Ejecuta el siguiente comando para abrir la interfaz de texto interactiva:

```bash
python -m app.tui
```
Abre una interfaz estilo terminal con botones interactivos. Ideal para quienes disfrutan el modo visual sin salir del terminal.

* Características:
- Interfaz visual en la terminal con botones interactivos.
- Ideal para quienes prefieren una experiencia más visual sin salir del terminal.

---

## 🖥️ Modo Web
Ejecuta el siguiente comando para iniciar la API REST:

```bash
python -m app.web
```

Endpoints disponibles:

- **GET /status** → Estado de contenedores, imágenes y volúmenes
- **GET /clean/basic** → Limpieza básica
- **GET /clean/advanced** → Limpieza avanzada (-a)
- **GET /clean/volumes** → Limpieza de volúmenes
- **GET /disk** → Uso de disco

Luego accede desde tu navegador a:
📡 http://localhost:5000

---

## 🐳 Ejecutar en Docker

1. Construir imagen

```bash
docker build -t docker-cleaner .
```

2. Ejecutar con acceso al Docker del host

```bash
docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock docker-cleaner
```

✅ Por defecto se ejecuta el modo CLI. Puedes cambiarlo modificando CMD en el Dockerfile.

---

## 📝 Logs

Todos los comandos ejecutados y errores quedan registrados en:

```bash
docker_cleaner.log
```

---

## 📊 Diagrama del flujo de ejecución

```
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
```

---

## 🔐 Configuración SSH para múltiples cuentas GitHub

Si trabajas con varias identidades (por ejemplo, una cuenta personal y una de organización), puedes configurar claves SSH separadas sin conflictos.

### ✅ Paso a paso para manejar varias identidades

1. Genera una nueva clave para la organización:

```bash
ssh-keygen -t ed25519 -C "github-automation-devops" -f ~/.ssh/id_ed25519_automation
```

2. Agrega la clave pública (.pub) a GitHub, en la organización correspondiente (Automtion-devops).

3. Crea o edita el archivo ~/.ssh/config con:

```bash
# Cuenta personal: jhenao-nex
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

# Organización: Automtion-devops
Host github-automation
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_automation
```

4. Usa github-automation como host remoto en tus repos de la organización:

```bash
git remote set-url origin git@github-automation:Automtion-devops/scripts.git
```

### 🔁 ¿Y si quiero volver a trabajar con mi cuenta personal?

Solo asegúrate de que el remote esté usando el host normal:

```bash
git remote set-url origin git@github.com:jhenao-nex/mi-repo.git
```

Este host usa por defecto la clave ~/.ssh/id_ed25519, correspondiente a tu cuenta personal.

### ✅ Resultado

Puedes trabajar con múltiples cuentas GitHub sin conflicto, simplemente cambiando el remote según corresponda:

- **github.com** → tu cuenta personal (jhenao-nex)
- **github-automation** → tu organización (Automtion-devops)

---

## ✍️ Autor

Jaime A. Henao A.
DevOps / Cloud Engineer ☁️ 🛠️
📧 Contacto disponible bajo solicitud

---

## 💡 Próximas mejoras

- Configuración por archivo .env
- Autenticación básica para API web
- Programador de tareas (cron-style)
- GUI desktop con Tkinter o Electron

¡Gracias por usar Docker Cleaner!
💥 Haz que tu entorno Docker vuelva a respirar.

