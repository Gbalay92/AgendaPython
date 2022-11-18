from Contacto import *
import json
# Opening JSON file
f = open('Contactos.json', "r+")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list



contacto= Contacto("ramon","r.canela@liceolapaz.net","01/01/1993")
#meter en el json
dictContacto={'nombre':contacto.nombre,
                'email':contacto.email,
                'fecha_de_nacimiento': contacto.fechaNac}

data['contacto'].append(dictContacto)
f.seek(0)
json.dump(data, f, indent=4)
for c in data['contacto']:
    print(c['nombre'])

# Closing file
f.close()
