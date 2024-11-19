from flask import *


page = Blueprint('page', __name__)

@page.route('/')
def index():
    
    return render_template('index.html')