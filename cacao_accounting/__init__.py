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

from flask import Flask
from cacao_accounting.auth import login

__name__ = "Cacao Accounting"
__license__ = "Apache Software License "
__version__ = "0.0.1"

DEVELOPMENT = True

def create_app(conf=None):
    """Aplication factory"""
    app = Flask(
        __name__,
        template_folder="cacao_accounting/templates",
        static_folder="cacao_accounting/static",
        instance_relative_config=False,
        )
    app.config.from_object(conf)
    app.register_blueprint(login)

    return app
