"""En este archivo se debe importar el archivo:
- ./controller.py
- ../util.py as util
- ../data/database.py as database
- ../tests/test_config.py as test_config ¿¿ donde esta la carpeta test ?? 
- ../tests/load_tests/ddos_simulation.py as ddos_simulation ¿¿ donde esta la carpeta test ??
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.controller.ejercicio_03
"""

# DUDA
# NO SE CUAL ES EL PAQUETE DEL ULTIMO ASSERT


# Completar
# source -> data, 
import sys
sys.path.append('D:\PABLO ESTUDIO\Facultad 2022\Soporte\REPO-ESTUDIO\python-frro-2022\practico_02')
import controller as controller
import source.util as util
import source.data.database as database
import config.test_config as test_config
import main








# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert controller.name == "controller"
assert test_config.name == "test_config"
#assert deploy_travis.name == "deploy_travis"
# NO MODIFICAR - FIN

# Este es el último ejercicio del TP2
