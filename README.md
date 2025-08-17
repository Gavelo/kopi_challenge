# Kopi Challenge - API de Chatbot de Debate 🤖💬

Este repositorio contiene la solución para el **"Kopi Challenge"**. El proyecto consiste en una API RESTful, construida con Python y FastAPI, que expone un chatbot diseñado para sostener un debate. El bot adopta una postura contraria a la afirmación inicial del usuario y su objetivo es persuadirlo, manteniendo la coherencia a lo largo de la conversación.

## Características Principales

* **IA de Debate:** Utiliza la API de Google Gemini para generar respuestas persuasivas y coherentes.
* **Postura Contraria:** El bot siempre adopta la postura opuesta a la del usuario para iniciar el debate.
* **Conversaciones con Estado:** Gestiona el historial de múltiples conversaciones de forma independiente utilizando Redis.
* **Contenerizado:** Totalmente empaquetado con Docker y orquestado con Docker Compose para un despliegue y ejecución sencillos.
* **Automatización:** Incluye un `Makefile` para simplificar tareas comunes como la instalación, ejecución y limpieza del entorno.

---

## Tech Stack

* **Lenguaje:** Python 3.11
* **Framework de API:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Base de Datos en Memoria:** Redis (para gestionar el historial de conversaciones)
* **IA Generativa:** Google Gemini API
* **Contenerización:** Docker & Docker Compose

---

## Configuración del Entorno

Para ejecutar este proyecto, es necesario configurar las variables de entorno.

#### 1. Prerrequisitos

Asegúrate de tener instalado **Docker** y **Docker Compose** en tu sistema.

* [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)

#### 2. Variables de Entorno

Crea un archivo llamado `.env` en la raíz del proyecto. Puedes copiar el archivo de ejemplo:
```bash
cp .env
```

##  Cómo Empezar

### Sigue estos pasos para levantar el proyecto en tu entorno local.

1. **Clona el repositorio**   
```bash
git clone <your-repo>
cd kopi-challenge
```   

2. **Levantar los Servicios**

Usa el Makefile para construir las imágenes y levantar los contenedores de la API y Redis.
```bash
make run
``` 

La API estará disponible en http://localhost:8000.

---

## Cómo Probar la API

Puedes interactuar con la API utilizando curl o cualquier cliente de API de tu preferencia.

### Iniciar una Nueva Conversación
Para comenzar un debate, envía una petición POST a /chat con conversation_id en null. El primer message establecerá el tema que el bot deberá rebatir.

```bash
curl -X POST "http://localhost:8000/chat" \
-H "Content-Type: application/json" \
-d '{
    "conversation_id": null,
    "message": "La inteligencia artificial superará a la humana en creatividad."
}'
``` 

Respuesta: Recibirás un JSON con un conversation_id nuevo. Cópialo para continuar la conversación.

Continuar una Conversación
Para enviar el siguiente mensaje, utiliza el conversation_id que recibiste en la respuesta anterior.

```bash
curl -X POST "http://localhost:8000/chat" \
-H "Content-Type: application/json" \
-d '{
    "conversation_id": "TU_CONVERSATION_ID_AQUI",
    "message": "Pero ya hay IAs que crean arte y música impresionantes."
}'
``` 

## Comandos del Makefile

Este proyecto incluye un Makefile para facilitar la gestión del ciclo de vida de la aplicación.
```bash
Comando	        Descripción
make help	    Muestra una lista de todos los comandos disponibles.
make install	Instala las dependencias de Python localmente usando pip (útil para desarrollo sin Docker).
make run	    Construye y levanta todos los servicios (API y Redis) usando docker-compose.
make down	    Detiene todos los servicios que se están ejecutando.
make clean	    Detiene los servicios, elimina los contenedores y las redes creadas.
``` 

