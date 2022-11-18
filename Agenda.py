import json
from Contacto import *

if __name__=="__main__":
    while(True):
        try:
            opcion=int(input("Agenda Contactos:\n1.Agregar\n2.Listar\n3.Eliminar\n4.Buscar\n0.Salir\nElija una opcion: "))
            match(opcion):
                case 1:
                    crearContacto('Contactos.json')
                case 2:
                    listarContactos('Contactos.json')
                case 3:
                    eliminarContacto('Contactos.json')
                case 4:
                    buscarContacto('Contactos.json')
                case 0:
                    exit()
        except TypeError:
            pass
