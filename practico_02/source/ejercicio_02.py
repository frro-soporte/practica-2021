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


# NO MODIFICAR - INICIO
import source

assert source.main.name == "main"
assert source.util.name == "util"
assert source.database.name == "database"
assert source.test_config.name == "test_config"
assert source.migrations.name == "migrations"
# NO MODIFICAR - FIN


# El siguiente ejercicio se encuentra en source/controller/ejercicio_03.py
