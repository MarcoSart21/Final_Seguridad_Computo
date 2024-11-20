from flask import *
from src.model.recuperar import *
from src.model.usuarios import *

recu = Blueprint('recu', __name__)

@recu.route('/recuperar', methods=['GET','POST'])
def recuperar():
    
    if request.method == 'POST':
        
        correo = request.form['email']
        codigo = secrets.token_urlsafe(6)
        
        recuperacion_contrasena(correo,codigo)
        
        session['correo_verificacion'] = correo
        session['codigo_verificacion'] = codigo
        
        
        return render_template('codigo.html')
    
    return render_template('recuperar.html')

@recu.route('/codigo', methods=['GET','POST'])
def codigo():
    
    if request.method == 'POST':
        
        codigo = request.form['codigo']
        codigo_correcto = session.get('codigo_verificacion')
        
        if codigo == codigo_correcto:
            return redirect(url_for('recu.cambio'))
        else:
            return redirect(url_for('recu.codigo'))
    
    return render_template('codigo.html')

@recu.route('/cambio', methods=['GET','POST'])
def cambio():
    
    if request.method == 'POST':
        
        contraseña = request.form['contrasena']
        correo = session.get('correo_verificacion')
        
        cambiar_contrasena(correo,contraseña)
        
        return render_template('iniciar.html')
    
    return render_template('cambio.html')