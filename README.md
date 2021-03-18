# Django Thinking Mobile

### A continuación se detalla como correr el código usando docker-compose.



### Instalación
Buildear la aplicación
```
docker-compose build
```


Levantar los containers
```
docker-compose up
```


Correr las migraciones
```
docker-compose exec thinking_mobile_web python3 manage.py migrate
```


Crear usuario de django (seguir los pasos)
```
docker-compose exec thinking_mobile_web python3 manage.py createsuperuser
```


### Correr los tests
```
doco exec thinking_mobile_web python3 manage.py test apps.redirect.tests.test.RedirectTestCase
```

