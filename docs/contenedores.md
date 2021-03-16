[![Contenedores](https://github.com/cacao-accounting/cacao-accounting/actions/workflows/container.yml/badge.svg)](https://github.com/cacao-accounting/cacao-accounting/actions/workflows/container.yml)
[![Docker Repository on Quay](https://quay.io/repository/cacaoaccounting/cacaoaccounting/status "Docker Repository on Quay")](https://quay.io/repository/cacaoaccounting/cacaoaccounting)

Existe una imagen de imagen OCI disponible para ejecutar Cacao Accounting en entornos de contenedores en [https://quay.io/repository/cacaoaccounting/cacaoaccounting](https://quay.io/repository/cacaoaccounting/cacaoaccounting).

## Crear un pod para ejecutar Cacao Accounting.

Podman es una herramienta para poder ejecutar pods, que son conjuntos de contenedores, con la cual 
podemos administrar Cacao Accounting utilizando contenedores, para instalar podman ejecutar:

```bash
# Fedora, CentOS ...
dnf -y install podman

# Debian, Ubuntu ...
apt install -y podman
```

Una vez podman esta instalado ejecutar Cacao Accounting en un pod ejecutando:

```bash
# Creamos un pod:
podman pod create --name cacao-pod -p 8080:8080 -p 3306:3306

# Creamos un volumen para almacenar la base de datos fuera del contenedor:
podman volume create cacao-database

# Creamos el contenedor para la base de datos:
podman run --pod cacao-pod --name cacaodb --volume cacao-database:/var/lib/mysql  \
    -e MYSQL_ROOT_PASSWORD=cacaodb \
    -e MYSQL_DATABASE=cacaodb \
    -e MYSQL_USER=cacaodb \
    -e MYSQL_PASSWORD=cacaodb \
    -d mysql

# Creamos el contenedor de la aplicación:
podman run --pod cacao-pod --name cacao \
    -e CACAO_ACCOUNTING=True \
    -e CACAO_KEY=nsjksldknsdlkdsljdn \
    -e CACAO_DB=mysql+pymysql://cacaodb:cacaodb@localhost:3306/cacaodb \
    -d quay.io/cacaoaccounting/cacaoaccounting
``` 
Luego de un momento la aplicación debera estar disponible en: http://localhost:8080, en caso de
que el contenedor no se ejecute puede reportar el error [aquí](https://github.com/cacao-accounting/cacao-accounting/issues)

Para acceder a la aplicación los datos de acceso son:

- Usuario: cacao
- Contraseña: cacao

```bash
Cacao Accounting es software en desarrollo no apto para uso en producción.
```

Para administrar el pod podemos ejecutar:

```bash
podman pod stop cacao-pod
podman pod start cacao-pod
```