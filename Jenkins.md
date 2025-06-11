# NIVEL BASICO: Conceptos iniciales

## JOBS
- Es una tarea automatizada -> Servidor Jenkins
    - Podria compilar
    - Ejecutar pruebas
    - Despliegue
    - O cualquier otro proceso
- Tipos de Jobs
    - Freestyle -> Es el mas basico y facil de ejecutar
    - Pipeline -> Usado para los flujos de CI CD -> Es mas avanzado con script en groovy
    - Multibranch pipeline -> Ideal para proyectos en git con varias ramas
    - Maven Projet -> Para proyectos maven

## BUILDS
- Es una ejecucion de un Job
- Cada vez que se haga una ejecucion se va a generar un build
    - Obtener el codigo fuente
    - Ejecutar los pasos que has definido
    - Registra la salida en el console
    - Guarda los artefactos (Opcional)
    - Muestra el resultado del build en el interfaz

## DISPARADORES AUTOMATICOS
- Polling SCM -> Revisar periodicamente si hay cambios en el repo de Github
- Webhook -> Relacionado con Github, Gitlab, Bitbucket, dispara un job cuando hay un cambio en el codigo
- Programacion cron -> Se ejecuta un Job en intervalos especificos
- Disparo por otro Job -> Un Job podria ejecutar otro Job cuando termine

## Plugins
- Son extenciones que se añaden a jenkins
- Y ello nos trae nuevas funcionalidades
- Plugins escenciales. Git Plugin, Maven Integration, Email extension

# NIVEL INTERMEDIO: Automatizacion y flujos de trabajo

## CONFIGURACION AVANZADA DE PROYECTOS FREESTYLE 🛠️🛠️
- Párametros en Jobs (ejemplo: seleccion de ramas)
- Uso de variables de entorno
    - BUILD_NUMBER: Numero de build actual
    - JOB_NAME: Nombre del Job que estas ejecutando
    - WORKSPACE: Directorio donde jenkins alamcena los archivos del job
    - GIT_COMMIT: Hash del commit si el job usa git
- Ejecucion de scripts en Bash, PowerShell o Python
- Configuracion de notificaciones (Email, Slack)
    - Para ello se configura el servidor SMTP

## INTEGRACION CON HERRAMIENTAS DE CONTROL DE VERSIONES
- Conexion con GitHub
- Configuracion de webhooks para disparadores automaticos
- Manejos de multiples ramas y pull requests

## AUTOMATIZACION DE PRUEBAS
- Integracion con herramientas de pruebas (JUnit, Selenium, pytest)
- Generacion de reportes de resultados
- Fallos condicionales: Que hacer si las pruebas fallan