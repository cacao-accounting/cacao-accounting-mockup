# Cacao Accounting

Aplicacion contable para micro, pequeñas y medianas empresas (MiPymes).

:warning: Aun es desarrollo temprano.

Requisitos:

  * [Nodejs](https://nodejs.org/en/) 12 o superior
  * [Yarn](https://yarnpkg.com/lang/en/) 1.12 o superior
  * [Python](https://www.python.org/downloads/) 3.8 o superior

  Este en un simple proyecto en Flask utilizando la funcion render_template() para mostrar en el navegador 
  plantillas utilizando Jinja2 como motor de renderizado.

## Iniciando proyecto:

Descarga el codigo fuente con:

```bash
git clone https://github.com/cacao-accounting/cacao-accounting-mockup.git
```

Para iniciar el proyecto es necesario seguir estos pasos:

### Crear un entorno virtual de python.

```bash
  python -m venv venv
  .\venv\Scripts\activate.bat # Windows
  source venv/bin/activate # Linux
```

### Instalar las dependencias:

```bash
# Python
  python -m pip install -r requirements.txt

# Nodejs
  yarn
```

Yarn es necesario para no tener incluir librerias de JavaScritp de terceros en el repositorio principal del proyecto.

## Iniciar

Para acceder al proyecto podemos utilizar el servidor web de desarrollo incluido en flask:

```bash
  python setup.py develop
  flask run
```

## Esquema de la base de datos

Para crear una base de datos sqlite con el esquema de la base de datos utilizar el comando:

```bash
  flask init-db
```
# Licencia.

Derechos de autor 2020 William José Moreno Reyes

Autorizado en virtud de la Licencia de Apache, Versión 2.0 (la "Licencia"); se
prohíbe utilizar este archivo excepto en cumplimiento de la Licencia. Podrá
obtener una copia de la Licencia en:

  http://www.apache.org/licenses/LICENSE-2.0

A menos que lo exijan las leyes pertinentes o se haya establecido por escrito,
el software distribuido en virtud de la Licencia se distribuye “TAL CUAL”, SIN
GARANTÍAS NI CONDICIONES DE NINGÚN TIPO, ya sean expresas o implícitas. Véase
la Licencia para consultar el texto específico relativo a los permisos y
limitaciones establecidos en la Licencia.