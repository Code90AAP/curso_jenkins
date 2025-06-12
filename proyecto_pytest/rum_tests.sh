#!/bin/bash

echo "Activando el entorno virtual"
source venv/Scripts/activate || exit 1

echo "Instalando dependencias"
pip install -r requirements.txt || exit 1

echo "Ejecutando pruebas con pytest"
pytest tests/ --junitxml=reports/test_results.xml --html=reports/test_results.html --self-contained-html exit 1

echo "Pruebas completadas. Resultados guardados en reports/test_results.xml y reports/test_results.html"