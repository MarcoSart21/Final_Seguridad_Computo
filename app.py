from flask import *
import random
import string
from src.controller.page_controller import *
from src.controller.recuperacion_controller import *
from src.controller.dash_controller import *



app = Flask(__name__, 
            template_folder='src/view/templates',
            static_folder='src/view/static')

caracteres = string.ascii_letters + string.digits + string.punctuation

clave = ''.join(random.choices(caracteres, k=10))

app.secret_key = clave

app.register_blueprint(page)
app.register_blueprint(recu)
app.register_blueprint(dash)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)