from src.model.conexion import *
import random

def registrar_usuario(nombre,correo,contrasena):

    id_usuario = random.randint(4, 9999)
    id_TUsuario = 1
    
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO Usuarios(Id_Usuario,Nombre,Correo,Contraseña,id_TUsuario) Values (?,?,?,?,?)",
        (id_usuario,nombre,correo,contrasena,id_TUsuario)
    )

    print("Agregado Exitosamente")

    cursor.commit()
    
    cursor.close()
    
def iniciar_sesion(email, password):    
    correo = str(email)
    contrasena = str(password)
    
    cursor = conexion.cursor()
    
    cursor.execute(
        """
            SELECT USUARIOS.Id_Usuario, USUARIOS.Nombre, USUARIOS.Correo, USUARIOS.Contraseña, USUARIOS.id_TUsuario, TP.Nombre FROM Usuarios
            INNER JOIN Tipo_Usuario AS TP ON Usuarios.id_TUsuario = TP.Id_TUsuario
            WHERE USUARIOS.Correo = ?
        """,
        (correo)
    )
    
    resultados_consulta = cursor.fetchall()
    
    if not resultados_consulta:
        print("Ningun Usuario")
        
        return False
    
    else:
        for resultado in resultados_consulta:
            if resultado[2] == correo and resultado[3] == contrasena:
                print("Sesion Iniciada con Exito")
                print(f"Bienvenido {resultado[1]}")
                
                datos = {
                    'id_TU' : resultado[4],
                    'nombre': resultado[1],
                    'correo': resultado[2],
                    'TUsuario': resultado[5]
                }
                
                print(datos)
                
                return datos
            else:
                return False
            
def cambiar_contrasena(correo,contrasena):
    
    cursor = conexion.cursor()
    
    cursor.execute(
        f"UPDATE Usuarios SET contraseña = ? WHERE Correo = ?;",
        (contrasena,correo)
    )
    
    cursor.commit()
    cursor.close()
    
    print("Actualizado Exitosamente")
    
    return True
    
def eliminar_usuario(correo):
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM Usuarios WHERE Correo = ?;",
        (correo)
    )

    print("Eliminado Exitosamente")

    cursor.commit()
    
    cursor.close()
    
# cambiar_contrasena('m4rcosw8@gmail.com','pollo')