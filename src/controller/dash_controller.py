from flask import *
from src.model.usuarios import *
from src.model.recuperar import *
from src.model.busquedas import *



dash = Blueprint('dash', __name__)

@dash.route('/eliminar', methods=['DELETE'])
def eliminar():

    return None