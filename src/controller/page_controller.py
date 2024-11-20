from flask import *
from src.model.usuarios import *
from src.model.recuperar import *
from src.model.busquedas import *



page = Blueprint('page', __name__)

@page.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')

@page.route('/iniciar', methods=['GET','POST'])
def iniciar():
    
    if request.method == 'POST':
        
        correo = request.form['email']
        contrasena = request.form['password']
        
        respuesta = iniciar_sesion(correo,contrasena)
        
        if respuesta == False:
            
            return redirect(url_for('page.iniciar'))
            
        else:
            if respuesta['id_TU'] == 1:
                session['usuario'] = respuesta
                return redirect(url_for('page.dashboard'))
            else:
                session['usuario'] = respuesta
                return redirect(url_for('page.perfil'))
    
    return render_template('iniciar.html')

@page.route('/cerrar')
def cerrar():
    
    session.pop('usuario', None)
    
    return redirect(url_for('page.index'))

@page.route('/registro', methods=['GET','POST'])
def registro():
    
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        correo = request.form['email']
        contrasena = request.form['password']
        
        registrar_usuario(nombre,correo,contrasena)
        
        return render_template('index.html')
    
    return render_template('registro.html')


@page.route('/perfil', methods=['GET','POST'])
def perfil():
    
    if request.method == 'POST':
        
        correo = request.form['correo']
        contraseña = request.form['contrasena_nueva']
        
        cambiar_contrasena(correo,contraseña)
        
        return redirect(url_for('page.perfil'))
    
    datos = session.get('usuario')
    
    return render_template('perfil.html', datos=datos)

@page.route('/dashboard')
def dashboard():
    
    datos = buscar_usuarios()
    roles = buscar_roles()
    
    usuario = session.get('usuario')
    
    return render_template('dashboard.html', datos=datos, roles=roles, usuario=usuario)
