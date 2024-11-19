from flask import *
from src.controller.page_controller import *

app = Flask(__name__, 
            template_folder='src/view/templates',
            static_folder='src/view/static')

app.register_blueprint(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)