# Copyright 2020 William José Moreno Reyes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Contributors:
# - William José Moreno Reyes

"""
Datos de ejemplo.
"""
from datetime import date
from cacao_accounting.database import db
from cacao_accounting.loggin import log

# pylint: disable=import-outside-toplevel


def _demo_usuarios():
    """Usuarios para demostracion"""
    from cacao_accounting.database import Usuario
    from cacao_accounting.auth import proteger_passwd

    log.debug("Creando usuarios de prueba.")
    usuarios = [
        Usuario(
            usuario="admin",
            correo_e="admin@cacao_accounting.io",
            clave_acceso=proteger_passwd("admin"),
        ),
        Usuario(
            usuario="ventas",
            correo_e="ventas@cacao_accounting.io",
            clave_acceso=proteger_passwd("ventas"),
        ),
        Usuario(
            usuario="compras",
            correo_e="compras@cacao_accounting.io",
            clave_acceso=proteger_passwd("compras"),
        ),
        Usuario(
            usuario="conta",
            correo_e="contabilidad@cacao_accounting.io",
            clave_acceso=proteger_passwd("conta"),
        ),
        Usuario(
            usuario="almacen",
            correo_e="almacen@cacao_accounting.io",
            clave_acceso=proteger_passwd("almacen"),
        ),
        Usuario(
            usuario="caja",
            correo_e="caja@cacao_accounting.io",
            clave_acceso=proteger_passwd("caja"),
        ),
    ]
    for usuario in usuarios:
        db.session.add(usuario)
    db.session.commit()


ENTIDAD_DEMO1 = {
    "entidad": "cacao",
    "razon_social": "Choco Sonrisas Sociedad Anonima",
    "nombre_comercial": "Choco Sonrisas",
    "id_fiscal": "J0310000000000",
    "moneda": "NIO",
    "tipo_entidad": "Sociedad",
    "correo_electronico": "info@chocoworld.com",
    "web": "chocoworld.com",
    "telefono1": "+505 8456 6543",
    "telefono2": "+505 8456 7543",
    "fax": "+505 8456 7545",
    "habilitada": True,
    "predeterminada": True,
    "status": "predeterminado",
}


ENTIDAD_DEMO2 = {
    "entidad": "cafe",
    "razon_social": "Mundo Cafe Sociedad Anonima",
    "nombre_comercial": "Mundo Cafe",
    "id_fiscal": "J0310000000001",
    "moneda": "USD",
    "tipo_entidad": "Sociedad",
    "correo_electronico": "info@mundocafe.com",
    "web": "mundocafe.com",
    "telefono1": "+505 8456 6542",
    "telefono2": "+505 8456 7542",
    "fax": "+505 8456 7546",
    "habilitada": True,
    "predeterminada": False,
    "status": "activo",
}

ENTIDAD_DEMO3 = {
    "entidad": "dulce",
    "razon_social": "Mundo Sabor Sociedad Anonima",
    "nombre_comercial": "Dulce Sabor",
    "id_fiscal": "J0310000000002",
    "moneda": "NIO",
    "tipo_entidad": "Sociedad",
    "correo_electronico": "info@chocoworld.com",
    "web": "chocoworld.com",
    "telefono1": "+505 8456 6543",
    "telefono2": "+505 8456 7543",
    "fax": "+505 8456 7545",
    "habilitada": False,
    "predeterminada": False,
    "status": "inactivo",
}


def _demo_entidad():
    """Entidad de demostración"""
    from cacao_accounting.contabilidad.registros.entidad import RegistroEntidad

    log.debug("Creando entidades de prueba.")
    instancia_entidad = RegistroEntidad()
    instancia_entidad.crear_registro_maestro(datos=ENTIDAD_DEMO1)
    instancia_entidad.crear_registro_maestro(datos=ENTIDAD_DEMO2)
    instancia_entidad.crear_registro_maestro(datos=ENTIDAD_DEMO3)


def _demo_unidades():
    """Unidades de Negocio de Demostración"""
    from cacao_accounting.database import Unidad

    log.debug("Cargando unidades de negocio de prueba.")
    unidades = [
        Unidad(
            nombre="Casa Matriz",
            entidad="cacao",
            unidad="matriz",
            status="activa",
        ),
        Unidad(
            nombre="Movil",
            entidad="cacao",
            unidad="movil",
            status="activa",
        ),
        Unidad(
            nombre="Masaya",
            entidad="cacao",
            unidad="masaya",
            status="inactiva",
        ),
    ]
    for unidad in unidades:
        db.session.add(unidad)
    db.session.commit()


CUENTA_PRUEBA_NIVEL01 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6",
    "nombre": "Cuenta Prueba Nivel 0",
    "grupo": True,
    "padre": None,
}

CUENTA_PRUEBA_NIVEL02 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1",
    "nombre": "Cuenta Prueba Nivel 1",
    "grupo": True,
    "padre": "6",
}

CUENTA_PRUEBA_NIVEL03 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1",
    "nombre": "Cuenta Prueba Nivel 2",
    "grupo": True,
    "padre": "6.1",
}

CUENTA_PRUEBA_NIVEL04 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1",
    "nombre": "Cuenta Prueba Nivel 3",
    "grupo": True,
    "padre": "6.1.1",
}

CUENTA_PRUEBA_NIVEL05 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 4",
    "grupo": True,
    "padre": "6.1.1.1",
}

CUENTA_PRUEBA_NIVEL06 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 5",
    "grupo": True,
    "padre": "6.1.1.1.1",
}

CUENTA_PRUEBA_NIVEL07 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 6",
    "grupo": True,
    "padre": "6.1.1.1.1.1",
}

CUENTA_PRUEBA_NIVEL08 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 7",
    "grupo": True,
    "padre": "6.1.1.1.1.1.1",
}

CUENTA_PRUEBA_NIVEL09 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 8",
    "grupo": True,
    "padre": "6.1.1.1.1.1.1.1",
}

CUENTA_PRUEBA_NIVEL10 = {
    "activa": True,
    "habilitada": True,
    "entidad": "cacao",
    "codigo": "6.1.1.1.1.1.1.1.1.1",
    "nombre": "Cuenta Prueba Nivel 9",
    "grupo": False,
    "padre": "6.1.1.1.1.1.1.1.1",
}


def _catalogo():
    from cacao_accounting.contabilidad.ctas import base, desarrollo, cargar_catalogos
    from cacao_accounting.contabilidad.registros.cuenta import RegistroCuentaContable

    log.debug("Cargando catalogos de cuentas.")
    cargar_catalogos(desarrollo, "cacao")
    cargar_catalogos(base, "dulce")
    cargar_catalogos(base, "cafe")
    CUENTA_CONTABLE = RegistroCuentaContable()
    for CTA in (
        CUENTA_PRUEBA_NIVEL01,
        CUENTA_PRUEBA_NIVEL02,
        CUENTA_PRUEBA_NIVEL03,
        CUENTA_PRUEBA_NIVEL04,
        CUENTA_PRUEBA_NIVEL05,
        CUENTA_PRUEBA_NIVEL06,
        CUENTA_PRUEBA_NIVEL07,
        CUENTA_PRUEBA_NIVEL08,
        CUENTA_PRUEBA_NIVEL09,
        CUENTA_PRUEBA_NIVEL10,
    ):
        CUENTA_CONTABLE.crear_registro_maestro(CTA)


CENTRO_COSTO_BASE = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": False,
    "codigo": "A00000",
    "nombre": "Centro Costos Predeterminado",
    "status": "activa",
}

CENTRO_COSTO_NIVEL00 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": True,
    "codigo": "B00000",
    "nombre": "Centro Costos Nivel 0",
    "status": "activa",
}

CENTRO_COSTO_NIVEL01 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": True,
    "codigo": "B00001",
    "nombre": "Centro Costos Nivel 1",
    "status": "activa",
    "padre": "B00000",
}

CENTRO_COSTO_NIVEL02 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": True,
    "codigo": "B00011",
    "nombre": "Centro Costos Nivel 2",
    "status": "activa",
    "padre": "B00001",
}

CENTRO_COSTO_NIVEL03 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": True,
    "codigo": "B00111",
    "nombre": "Centro Costos Nivel 3",
    "status": "activa",
    "padre": "B00011",
}

CENTRO_COSTO_NIVEL04 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": True,
    "codigo": "B01111",
    "nombre": "Centro Costos Nivel 4",
    "status": "activa",
    "padre": "B00111",
}

CENTRO_COSTO_NIVEL05 = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cacao",
    "grupo": False,
    "codigo": "B11111",
    "nombre": "Centro Costos Nivel 5",
    "status": "activa",
    "padre": "B01111",
}

CENTRO_COSTO_CAFE = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "cafe",
    "grupo": False,
    "codigo": "A00000",
    "nombre": "Centro Costos Predeterminado",
    "status": "activa",
}

CENTRO_COSTO_DULCE = {
    "activa": True,
    "predeterminado": True,
    "habilitada": True,
    "entidad": "dulce",
    "grupo": False,
    "codigo": "A00000",
    "nombre": "Centro Costos Predeterminado",
    "status": "activa",
}


def _centros_de_costos():
    from cacao_accounting.contabilidad.registros.ccosto import RegistroCentroCosto

    CENTRO_DE_COSTO = RegistroCentroCosto()
    log.debug("Cargando centros de costos.")
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_BASE)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL00)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL01)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL02)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL03)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL04)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_NIVEL05)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_CAFE)
    CENTRO_DE_COSTO.crear_registro_maestro(datos=CENTRO_COSTO_DULCE)


PROYECTO01 = {
    "habilitado": True,
    "entidad": "cacao",
    "codigo": "PTO001",
    "nombre": "Proyecto Prueba",
    "fechainicio": date(year=2020, month=6, day=5),
    "fechafin": date(year=2020, month=9, day=5),
    "presupuesto": 10000,
    "status": "abierto",
}


def _proyectos():
    from cacao_accounting.contabilidad.registros.proyecto import RegistroProyecto

    PROYECTO = RegistroProyecto()
    log.debug("Creando proyectos de pruebas.")
    PROYECTO.crear_registro_maestro(datos=PROYECTO01)


MONEDA01 = {
    "codigo": "custom",
    "nombre": "Dolar Paralelo",
    "decimales": 4,
    "activa": True,
    "predeterminada": False,
}


def _monedas():
    from cacao_accounting.contabilidad.registros.moneda import RegistroMoneda

    MONEDA = RegistroMoneda()
    log.debug("Creando monedas de prueba.")
    MONEDA.crear_registro_maestro(datos=MONEDA01)


TASA_CAMBIO01 = {
    "base": "NIO",
    "destino": "USD",
    "tasa": 34.5984,
    "fecha": date(year=2021, month=6, day=30),
}


def _tasas_de_cambio():
    from cacao_accounting.contabilidad.registros.tasa_cambio import RegistroTasaCambio

    TASA_CAMBIO = RegistroTasaCambio()
    log.debug("Creando tasas de cambio de pruebas.")
    TASA_CAMBIO.crear_registro_maestro(datos=TASA_CAMBIO01)


def master_data():
    log.debug("Iniciando carga de master data de pruebas.")
    _demo_usuarios()
    _demo_entidad()
    _demo_unidades()
    _centros_de_costos()
    _proyectos()
    _monedas()
    _tasas_de_cambio()
    _catalogo()
    log.debug("Master data de prueba creada correctamente.")


def _periodo_contable():
    from cacao_accounting.contabilidad.registros.periodo import RegistroPeriodoContable

    PERIODO = RegistroPeriodoContable()
    log.debug("Creando periodos contables de prueba.")
    PERIODO.crear_registro_maestro(
        {
            "entidad": "cacao",
            "nombre": "2019",
            "status": "cerrado",
            "habilitada": False,
            "inicio": date(year=2019, month=1, day=1),
            "fin": date(year=2019, month=12, day=31),
        }
    )
    PERIODO.crear_registro_maestro(
        {
            "entidad": "cacao",
            "nombre": "2020",
            "status": "actual",
            "habilitada": False,
            "inicio": date(year=2020, month=1, day=1),
            "fin": date(year=2020, month=12, day=31),
        }
    )
    PERIODO.crear_registro_maestro(
        {
            "entidad": "cacao",
            "nombre": "2021",
            "status": "abierto",
            "habilitada": False,
            "inicio": date(year=2021, month=1, day=1),
            "fin": date(year=2021, month=12, day=31),
        }
    )


def transacciones():
    _periodo_contable()
    log.debug("Transacciones de Pruebas Creadas correstamente.")


def demo_data():
    master_data()
    transacciones()
