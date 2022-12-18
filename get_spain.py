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
        spain[comunidad] = {}

    provincia = normalize(item['fields']['texto'])
    spain[comunidad][provincia] = []
    for objeto in json_municipios:
        provincias = normalize(objeto['prov'])
        municipio = normalize(objeto['loc'])
        if provincias == provincia:
            spain[comunidad][provincia].append(municipio) 

print(spain)