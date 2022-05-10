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

# Completar
import source.util as util
import source.data.database as database
import config.test_config as test_config
import config.db_config.migrations as migrations
import main

# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert test_config.name == "test_config"
assert migrations.name == "migrations"
# NO MODIFICAR - FIN


# El siguiente ejercicio se encuentra en source/controller/ejercicio_03.py
