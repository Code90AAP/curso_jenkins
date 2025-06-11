#!/bin/bash

echo "Ingresando al directorio del proyecto"
cd proyecto_pytest

echo "Activando el entorno virtual"
source venv/bin/activate

echo "Instalando dependencias"
pip install -r requirements.txt

echo "Ejecutando pruebas con pytest"
pytest tests/ --junitxml=reports/test_results.xml --html=reports/test_results.html --self-contained-html

echo "Pruebas completadas. Resultados guardados en reports/test_results.xml y reports/test_results.html"