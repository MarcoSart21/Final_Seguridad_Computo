from src.model.conexion import *
import random

def agregar_roles(nombre):
    
    print(nombre)

    id_usuario = random.randint(4, 9999)
    id_TUsuario = 1
    
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO Tipo_Usuario(Id_TUsuario,Nombre) Values (?,?)",
        (id_usuario,nombre)
    )

    print("Agregado Exitosamente")

    cursor.commit()
    
    cursor.close()