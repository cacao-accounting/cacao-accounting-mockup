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

from cacao_accounting.database import Entidad
from cacao_accounting.exceptions import TransactionError
from cacao_accounting.transaccion import Transaccion


def validar_entidad_activa(transaccion: Transaccion) -> bool:
    if transaccion.datos.get("entidad", None):  # type: ignore[union-attr]
        entidad = Entidad.query.filter_by(entidad=transaccion.datos["entidad"]).first()  # type: ignore[index]
        if entidad.status != "inactiva":
            return True
        else:
            raise TransactionError("Entidad se encuentra inactiva.")
    else:
        return True


VALIDACIONES_PREDETERMINADAS: list = []
