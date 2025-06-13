@echo off
cd /d %~dp0

cd ..

cd proyecto_pytest

:: Crear entorno virtual si no existe
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
)

:: Activar entorno virtual
call venv\Scripts\activate.bat

:: Instalar dependencias si existe requirements.txt
if exist requirements.txt (
    pip install --upgrade pip
    pip install -r requirements.txt
)

:: Ejecutar pruebas
pytest
