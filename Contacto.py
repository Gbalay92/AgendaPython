import json

def pedirDatos(nombre, email, fechaNac):
    if(nombre):
        x = input("introduzca el nombre : ")
        if(email):
            y = input("introduzca el email: ")
            if(fechaNac):
                z = input("introduzca la fecha de nacimiento: ")
                return x,y,z
            else:
                return x, y
        else:
            return x
class Contacto():
    def __init__(self, nombre, email, fechaNac):
        self.nombre = nombre
        self.email = email
        self.fechaNac = fechaNac

def crearContacto(archivo):
    nombre, email, fecha=pedirDatos(True, True, True)
    contacto= Contacto(nombre, email, fecha)
    #meter en el json
    dictContacto={'nombre':contacto.nombre,
                'email':contacto.email,
                'fecha_de_nacimiento': contacto.fechaNac}
    f=open(archivo, "r+")
    data = json.load(f)
    data['contacto'].append(dictContacto)
    f.seek(0)
    json.dump(data, f, indent=4)
def listarContactos(archivo):
    with open(archivo, 'r+') as json_file:
        dict = json.load(json_file)
    for contacto in dict['contacto']:
        print(contacto['nombre'], contacto['email'], contacto['fecha_de_nacimiento'])

def eliminarContacto(archivo):
    busqueda=input("introduzca nombre o email: ")
    with open(archivo, "r+") as json_file:
        dict=json.load(json_file)
        i=None
        json_file.close
    for contacto in dict['contacto']:
        if(contacto['nombre']==busqueda):
            print(contacto['nombre'], contacto['email'], contacto['fecha_de_nacimiento'])
            i=input('introduzca el email para confirmar(si no quiere eliminar este contacto pulse enter): ')
            continue
        if(contacto['email']==i or contacto['email']==busqueda):
                dict['contacto'].remove(contacto)
                with open(archivo, "w") as json_file2:
                    json.dump(dict, json_file2, indent=4)
                    break
        else:
            print("No coincide")  
            break
        #buscar por nombre o email
        #si se busca por nombre listar si hay varios iguales
        #eliminar ese objeto
    

def buscarContacto(archivo):
    with open(archivo, 'r') as json_file:
        dict = json.load(json_file)
    busqueda=input("Introduzca nombre o email: ")
    for contacto in dict['contacto']:
        if (busqueda==contacto['nombre'] or busqueda==contacto['email']):
            print(contacto['nombre'], contacto['email'], contacto['fecha_de_nacimiento'])
    
        
        
        
    