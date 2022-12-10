import re
import json
import requests

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
    return s.lower()

def checkstatus(url):
    try:
        rest_response = requests.get(url)
        return rest_response.status_code
    except requests.ConnectionError:
        return "failed to connect"

def unzip_json(url):
    return json.loads(requests.get(url).content)

def generate_post_data(input_json, genre, country='spain', city=None, state=None, muni=None):
    json_object = {}
    json_object['username'] = input_json['name']['es']
    json_object['description'] = input_json['description']['es']
    for condition in ['<p>', '</p>', '<span>', '</span>', '<br>', '<br />', '/<\/?span[^>]*>/g']:
        if re.search('br', condition):
            json_object['description'] = json_object['description'].replace(condition, '\n')
        else:
            json_object['description'] = json_object['description'].replace(condition, '')
    # json_object['description'] = json_object['description'].replace('<p>', '').replace('</p>', '\n').replace('<br>', '\n').replace('<br />', '\n').replace('<span>', )
    json_object['age'] = input_json['age'] if 'age' in input_json else '18'
    json_object['phone'] = input_json['phoneNumber']
    json_object['photos'] = input_json['featuredImages']if 'featuredImages' in input_json else []
    json_object['addressCountry'] = country
    json_object['addressCity'] = city
    json_object['addressState'] = state
    json_object['addressZone'] = input_json['zone'] if 'zone' in input_json else None
    json_object['addressMuni'] = muni
    json_object['coordinates'] = input_json['coordinates'] if 'coordinates' in input_json else None
    json_object['genre'] = genre
    json_object['nationality'] = input_json['country'] if 'country' in input_json else None
    json_object['verifiedPhotos'] = input_json['verifiedPhotos']
    json_object['isWorker'] = True
    json_object['isDeleted'] = False
    json_object['show_phone'] = False
    json_object['services'] = input_json['services']
    return json_object

def upload_photo_from_user(user_id, photos, videos, verified):
    json_object = {}
    json_object['user'] = user_id
    json_object['photo'] = photos
    json_object['video'] = videos
    json_object['verified'] = verified
    return json_object

def print_update(instr):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    print(instr)
    print(LINE_UP, end=LINE_CLEAR)

class checkspain:
    def __init__(self, spain_json, comunidad, provincia, municipio=None):
        if municipio is not None:
            self.municipio = municipio
        self.spain = spain_json
        self.comunidad = comunidad
        self.provincia = provincia
        self.municipio = municipio
        self.result = "delete"

    def checkProvincia(self):
        provincia_normalized = normalize(self.provincia)
        full_url = f"https://valenciacitas-v2.s3.eu-west-3.amazonaws.com/data/{provincia_normalized}.gzip"
        self.provincia_check_url = checkstatus(full_url)
        print_update("Añadiendo provincia: " + self.provincia)


        if self.provincia_check_url == 200:
            gzip_uncompressed = unzip_json(full_url)
            self.spain[self.comunidad]['provincias'][self.provincia]['girls'] = gzip_uncompressed['girls']
            self.spain[self.comunidad]['provincias'][self.provincia]['guysAndTrans'] = gzip_uncompressed['guysAndTrans']
            self.result = self.spain[self.comunidad]['provincias'][self.provincia]

    def checkMunicipios(self):
        municipio_normalized = normalize(self.municipio)
        full_url = f"https://valenciacitas-v2.s3.eu-west-3.amazonaws.com/data/{municipio_normalized}.gzip"
        self.municipio_check_url = checkstatus(full_url)
        print_update("Añadiendo municipio: " + self.municipio)

        if self.municipio_check_url == 200:
            gzip_uncompressed = unzip_json(full_url)
            self.spain[self.comunidad]['provincias'][self.provincia]['municipios'][self.municipio]['girls'] = gzip_uncompressed['girls']
            self.spain[self.comunidad]['provincias'][self.provincia]['municipios'][self.municipio]['guysAndTrans'] = gzip_uncompressed['guysAndTrans']
            self.result = self.spain[self.comunidad]['provincias'][self.provincia]['municipios'][self.municipio]
