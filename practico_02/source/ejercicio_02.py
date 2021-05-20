"""En este archivo se debe importar el archivo:
- ./util.py as util
- ./data/database.py as database
- ../config/test_config.py as test_config
- ../config/db_config/migrations.py as migrations
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.ejercicio_02
"""

import util as util
from data import database as database
import practico_02.config.test_config as test_config
import practico_02.config.db_config.migrations as migrations
import practico_02.main as main



# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert test_config.name == "test_config"
assert migrations.name == "migrations"
# NO MODIFICAR - FIN


# El siguiente ejercicio se encuentra en source/controller/ejercicio_03.py
