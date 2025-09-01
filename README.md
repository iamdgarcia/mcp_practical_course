# MCP Python Demo

Ejemplo práctico de cómo usar el **Model Context Protocol (MCP)** con Python.  
Este repo incluye un servidor básico, un servidor conectado a SQLite y un cliente de prueba.  

MCP es un estándar abierto creado por Anthropic que permite conectar modelos de lenguaje (LLMs) con datos y herramientas externas de forma estandarizada.  
Piensa en él como el **USB-C de la inteligencia artificial**.

---

## 📂 Contenido del repo

- `src/servidor.py` → Servidor MCP básico (tool `sumar`)
- `src/servidor_bd.py` → Servidor MCP conectado a SQLite (tool `get_top_chatters`)
- `src/cliente.py` → Cliente MCP que lanza el servidor como subproceso y prueba las tools
- `src/init_sqlite.py` → Script para inicializar la base de datos `community.db`
- `data/community.db` → Base de datos SQLite generada con datos de ejemplo
- `Dockerfile` → Para desplegar en DigitalOcean, Render, Fly.io, etc.
- `Procfile` → Compatibilidad con Heroku-like PaaS
- `requirements.txt` → Dependencias (`mcp`, `python-dotenv`)

---

## 🚀 Instalación local

### 1. Clonar el repo
```bash
git clone https://github.com/iamdgarcia/mcp-practical-course.git
cd mcp-practical-course
````

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate    # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Inicializar la base de datos de ejemplo

```bash
python src/init_sqlite.py
```

---

## 🧪 Uso

### Servidor básico (calculadora)

```bash
python src/servidor.py
```

### Servidor con base de datos

```bash
python src/servidor_bd.py
```

### Cliente de prueba

Edita en `src/cliente.py` qué servidor quieres lanzar (`servidor.py` o `servidor_bd.py`) y ejecuta:

```bash
python src/cliente.py
```

Ejemplo de salida con `servidor_bd.py`:

```
=== Herramientas disponibles ===
- get_top_chatters: Obtiene la lista de usuarios ordenados por mensajes enviados
===============================

Resultado: [{'name': 'Alice', 'messages': 120}, {'name': 'Bob', 'messages': 75}, {'name': 'Carlos', 'messages': 50}]
```

---

## 🐳 Docker

Construir y correr el contenedor:

```bash
docker build -t mcp-python-demo .
docker run -p 8080:8080 --env-file .env mcp-python-demo
```

---

## 🌐 Despliegue

Ejemplo con **DigitalOcean App Platform**:

1. Conecta este repo a tu cuenta de DO.
2. DO detectará el `Dockerfile`.
3. Exponer el puerto `8080` (la app también puede leer `$PORT`).
4. Añade variables de entorno necesarias en el panel de configuración.

---

## 🔒 Buenas prácticas

* No expongas tu servidor MCP sin control → usa autenticación o proxys.
* Guarda credenciales en `.env` y **no las subas al repo**.
* Actualiza dependencias (`pip install -U mcp`).
* Valida entradas de usuario antes de usarlas en queries SQL.

---

## 📖 Referencias

* [Model Context Protocol (oficial)](https://modelcontextprotocol.io/)
* [Python SDK en GitHub](https://github.com/modelcontextprotocol/python-sdk)
* [Guía en Medium (Mostafa Wael)](https://mostafawael.medium.com/demystifying-the-model-context-protocol-mcp-with-python-a-beginners-guide-0b8cb3fa8ced)
* [Hosting con Docker en DigitalOcean (Daniel García)](https://iamdgarcia.medium.com/how-to-host-your-python-web-app-on-digitalocean-with-docker-970ccedc7812)

---

## 📜 Licencia

Este proyecto está bajo licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente.

