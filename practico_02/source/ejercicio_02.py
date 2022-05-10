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
# CON EL -M SOLO FUNCIONA SI ESTOY EN LA CARPETA SOURCE, SI ME PARO EN PRACTICO_02 NO ME ANDA
# 


# Completar

import sys
sys.path.append('D:\PABLO ESTUDIO\Facultad 2022\Soporte\REPO-ESTUDIO\python-frro-2022\practico_02')
sys.path.append('D:\PABLO ESTUDIO\Facultad 2022\Soporte\REPO-ESTUDIO\python-frro-2022\practico_02\config')
from source import util
import data.database as database
import main as main
import config.test_config as test_config
import config.db_config.migrations as migrations

# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert test_config.name == "test_config"
assert migrations.name == "migrations"
# NO MODIFICAR - FIN



# El siguiente ejercicio se encuentra en source/controller/ejercicio_03.py