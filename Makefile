.PHONY: help install test run down clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install  - Instala las dependencias necesarias."
	@echo "  make run      - Levanta los servicios con Docker Compose."
	@echo "  make down     - Detiene los servicios."
	@echo "  make clean    - Detiene los servicios y elimina los contenedores."

install:
	@if ! command -v python3 &> /dev/null; then \
		echo "Error: python3 no está instalado. Por favor, instálalo para continuar."; \
		exit 1; \
	fi
	pip install -r requirements.txt
	@echo "Dependencias instaladas."

run:
	@if ! command -v docker &> /dev/null; then \
		echo "Error: Docker no está instalado. Por favor, instálalo para continuar."; \
		exit 1; \
	fi
	docker-compose up --build

down:
	docker-compose down

clean:
	docker-compose down -v --rmi local