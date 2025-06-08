# JOBS
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

# BUILDS
- Es una ejecucion de un Job
- Cada vez que se haga una ejecucion se va a generar un build
    - Obtener el codigo fuente
    - Ejecutar los pasos que has definido
    - Registra la salida en el console
    - Guarda los artefactos (Opcional)
    - Muestra el resultado del build en el interfaz

# DISPARADORES AUTOMATICOS
- Polling SCM -> Revisar periodicamente si hay cambios en el repo de Github
- Webhook -> Relacionado con Github, Gitlab, Bitbucket, dispara un job cuando hay un cambio en el codigo
- Programacion cron -> Se ejecuta un Job en intervalos especificos
- Disparo por otro Job -> Un Job podria ejecutar otro Job cuando termine