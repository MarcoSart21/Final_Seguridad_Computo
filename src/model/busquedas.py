from src.model.conexion import *

def buscar_usuarios():
    
    cursor = conexion.cursor()
    
    cursor.execute(
        """
            SELECT USUARIOS.Id_Usuario, USUARIOS.Nombre, USUARIOS.Correo, USUARIOS.Contraseña, USUARIOS.id_TUsuario, TP.Nombre FROM Usuarios
            INNER JOIN Tipo_Usuario AS TP ON Usuarios.id_TUsuario = TP.Id_TUsuario
        """
    )
    
    resultados_consulta = cursor.fetchall()
    
    if not resultados_consulta:
        print("Ningun Usuario")
        
        return False
    
    else:
        clientes = []
        for resultado in resultados_consulta:
            datos = {
                'id_TU' : resultado[4],
                'nombre': resultado[1],
                'correo': resultado[2],
                'TUsuario': resultado[5]
            }
            clientes.append(datos)
            
        return clientes
    
def buscar_roles():
    
    cursor = conexion.cursor()
    
    cursor.execute(
        """
            Select * from Tipo_Usuario;
        """
    )
    
    resultados_consulta = cursor.fetchall()
    
    if not resultados_consulta:
        print("Ningun Usuario")
        
        return False
    
    else:
        roles = []
        for resultado in resultados_consulta:
            datos = {
                'id' : resultado[0],
                'rol': resultado[1],
            }
            roles.append(datos)
            
        return roles
    
        