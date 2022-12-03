import json
import requests
from gzip import decompress

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
        # prints the int of the status code. Find more at httpstatusrappers.com :)
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
    for provincia in spain[comunidad]['provincias']:
        print(provincia)
        full_url = "https://valenciacitas-v2.s3.eu-west-3.amazonaws.com/data/{}.gzip".format(normalize(provincia).lower())
        spain[comunidad]['provincias'][provincia]['url'] = full_url
        spain[comunidad]['provincias'][provincia]['urls_status'] = checkstatus(full_url)
        if spain[comunidad]['provincias'][provincia]['urls_status'] == 200:
            print("Esta provincia tiene un json")
            gzip_uncompressed = unzip_json(full_url)
            spain[comunidad]['provincias'][provincia]['girls'] = gzip_uncompressed['girls']
            spain[comunidad]['provincias'][provincia]['guysAndTrans'] = gzip_uncompressed['guysAndTrans']
        if spain[comunidad]['provincias'][provincia]['urls_status'] == 200:
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
                print(data)
                r = requests.post("http://localhost:8000/api/users/", json=data)
