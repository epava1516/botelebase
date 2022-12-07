import json
import requests
from library.stealfuncs import normalize, checkspain, print_update, generate_post_data

with open('provincias.json') as f:
    json_provincias = json.load(f)

with open('lista_municipios.json') as f:
    json_municipios = json.load(f)

spain = {}
for item in json_provincias:
    comunidad = normalize(item['fields']['ccaa'])
    if comunidad not in spain:
        spain[comunidad] = {"provincias": {}}

    provincia = normalize(item['fields']['texto'])
    spain[comunidad]['provincias'][provincia] = {"municipios": {}}
    for objeto in json_municipios:
        provincias = normalize(objeto['prov'])
        municipio = normalize(objeto['loc'])
        if provincias == provincia:
            spain[comunidad]['provincias'][provincia]["municipios"][municipio] = {}

for comunidad in spain.copy():
    print("Comunidad: " + comunidad)
    # recorremos todas las provincias
    for provincia in spain[comunidad]['provincias'].copy():
        homonimo = False

        # recorremos todos los municipios
        for municipio in spain[comunidad]['provincias'][provincia]['municipios'].copy():
            # si el municipio se llama igual a la provincia luego nos saltamos el check de la provincia
            if municipio == provincia:
                homonimo = True
            check_municipio = checkspain(spain,comunidad,provincia,municipio)
            check_municipio.checkMunicipios()
            #Eliminamos aquellos municipios que no arrojen resultado
            if check_municipio.result == 'delete':
                spain[comunidad]['provincias'][provincia]['municipios'].pop(municipio)
                print_update("Eliminando municipio sin clientes: " + municipio)
            #Registramos el resultado de los municipios que si
            if check_municipio.result != 'delete':
                spain[comunidad]['provincias'][provincia]['municipios'][municipio] = check_municipio.result

        if len(spain[comunidad]['provincias'][provincia]['municipios']) == 0:
            spain[comunidad]['provincias'][provincia].pop('municipios')
            print_update("Eliminando provincia sin clientes: " + provincia)

        # Comprobamos si existiera una URL para la provincia
        check_provincia = checkspain(spain,comunidad, provincia)
        check_provincia.checkProvincia()

        if check_provincia.result == 'delete':
            if 'municipios' in spain[comunidad]['provincias'][provincia]:
                continue

            if 'municipios' not in spain[comunidad]['provincias'][provincia]:
                spain[comunidad]['provincias'].pop(provincia)

        if check_provincia.result != 'delete':
            if homonimo:
                continue
            if not homonimo:
                spain[comunidad]['provincias'][provincia] = check_provincia.result

    for provincia in spain[comunidad]['provincias'].copy():
        if len(spain[comunidad]['provincias'][provincia])==0:
            spain[comunidad]['provincias'].pop(provincia)


    if len(spain[comunidad]['provincias']) == 0:
        spain.pop(comunidad)
        print("Eliminando comunidad sin clientes: " + comunidad + "\n")

for comunidad in spain:
    for provincia in spain[comunidad]['provincias']:
        for municipio in spain[comunidad]['provincias'][provincia]['municipios']:
            for user in spain[comunidad]['provincias'][provincia]['municipios'][municipio]['girls']:
                URL = "http://localhost:8000/api/users/"
                data = generate_post_data(user,genre="M",city=comunidad,state=provincia,muni=municipio)
                response = requests.post(URL, json=data)
                print(response.text)

        for municipio in spain[comunidad]['provincias'][provincia]['municipios']:
            for user in spain[comunidad]['provincias'][provincia]['municipios'][municipio]['guysAndTrans']:
                if 'isMan' in user:
                    if user['isMan']:
                        URL = "http://localhost:8000/api/users/"
                        data = generate_post_data(user,genre="H",city=comunidad,state=provincia,muni=municipio)
                        response = requests.post(URL, json=data)
                        # print(response.text)
                    else:
                        URL = "http://localhost:8000/api/users/"
                        data = generate_post_data(user,genre="T",city=comunidad,state=provincia,muni=municipio)
                        response = requests.post(URL, json=data)
                        # print(response.text)
