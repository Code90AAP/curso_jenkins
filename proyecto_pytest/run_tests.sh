#!/bin/bash

echo "Activando el entorno virtual"

if [ ! -d "venv" ]; then
    echo "El entorno virtual no existe. Creando uno nuevo..."
    python -m venv venv || exit 1
fi

source venv/Scripts/activate || exit 1

echo "Instalando dependencias"
pip install --upgrade pip || exit 1
pip install -r requirements.txt || exit 1

echo "Ejecutando pruebas con pytest"
pytest tests/ --junitxml=reports/test_results.xml --html=reports/test_results.html --self-contained-html || exit 1

echo "Pruebas completadas. Resultados guardados en reports/test_results.xml y reports/test_results.html"