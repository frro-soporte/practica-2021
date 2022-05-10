"""En este archivo se debe importar el archivo:
- ./controller.py
- ../util.py as util
- ../data/database.py as database
- ../tests/test_config.py as test_config
- ../tests/load_tests/ddos_simulation.py as ddos_simulation
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.controller.ejercicio_03
"""

# Completar
import source.controller.controller as controller
import source.util as util
import source.data.database as database
import config.test_config as test_config
import config.ci_cd.deploy_travis as deploy_travis
import main

# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert controller.name == "controller"
assert test_config.name == "test_config"
assert deploy_travis.name == "deploy_travis"
# NO MODIFICAR - FIN

# Este es el último ejercicio del TP2
