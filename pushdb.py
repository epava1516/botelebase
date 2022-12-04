import json
import requests

f = open('provincias.json')

json_provincias = json.load(f)

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return(s)

def checkstatus(url):
    try:
        r = requests.get(url)
        return(r.status_code)
    except requests.ConnectionError:
        return("failed to connect")

def unzip_json(url):
    return(json.loads(requests.get(url).content))


spain = {}
for item in json_provincias:
    if item['fields']['ccaa'] not in spain:
        spain[item['fields']['ccaa']] = {}
        spain[item['fields']['ccaa']]['provincias'] = {}

    spain[item['fields']['ccaa']]['provincias'][item['fields']['texto']] = {}

for comunidad in spain:
    print(comunidad)
    for idx, provincia in enumerate(spain[comunidad]['provincias']):
        full_url = "https://valenciacitas-v2.s3.eu-west-3.amazonaws.com/data/{}.gzip".format(normalize(provincia).lower())
        if checkstatus(full_url) != 200 && idx == len()
        if checkstatus(full_url) == 200:
            print(provincia)
            print("Esta provincia tiene un json")
            gzip_uncompressed = unzip_json(full_url)
            spain[comunidad]['provincias'][provincia]['girls'] = gzip_uncompressed['girls']
            spain[comunidad]['provincias'][provincia]['guysAndTrans'] = gzip_uncompressed['guysAndTrans']
            for girl in spain[comunidad]['provincias'][provincia]['girls']:
                url = "http://localhost:8000/api/users/"
                data = {}
                data['username'] = girl['name']['es']
                data['age'] = 18
                data['phone'] = girl['phoneNumber']
                data['email'] = "paredes1516@gmail.com"
                data['addressCity'] = provincia
                data['addressCountry'] = 'Spain'
                data['addressState'] = 'comunidad'
                data['genre'] = 'M'
                data['isWorker'] = True
                data['isDeleted'] = False
                data['show_phone'] = False
                r = requests.post(url, json=data)
            for other in spain[comunidad]['provincias'][provincia]['guysAndTrans']:
                # print(other)
                if 'isMan' in other:
                    if other['isMan']:
                        url = "http://localhost:8000/api/users/"
                        data = {}
                        data['username'] = other['name']['es']
                        data['age'] = 18
                        data['phone'] = other['phoneNumber']
                        data['email'] = "paredes1516@gmail.com"
                        data['addressCity'] = provincia
                        data['addressCountry'] = 'Spain'
                        data['addressState'] = 'comunidad'
                        data['genre'] = 'H'
                        data['isWorker'] = True
                        data['isDeleted'] = False
                        data['show_phone'] = False
                        r = requests.post(url, json=data)
                        # print(r.text)
                    else:
                        url = "http://localhost:8000/api/users/"
                        data = {}
                        data['username'] = other['name']['es']
                        data['age'] = 18
                        data['phone'] = other['phoneNumber']
                        data['email'] = "paredes1516@gmail.com"
                        data['addressCity'] = provincia
                        data['addressCountry'] = 'Spain'
                        data['addressState'] = 'comunidad'
                        data['genre'] = 'T'
                        data['isWorker'] = True
                        data['isDeleted'] = False
                        data['show_phone'] = False
                        r = requests.post(url, json=data)
                # else:
                #     print(list(other.keys()))
