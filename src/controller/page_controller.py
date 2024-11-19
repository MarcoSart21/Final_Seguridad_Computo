from flask import *


page = Blueprint('page', __name__)

@page.route('/')
def index():
    return render_template('index.html')

@page.route('/registro')
def registro():
    return render_template('registro.html')

@page.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

@page.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
