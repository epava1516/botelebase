import re
import requests
from library.stealfuncs import normalize, checkspain, print_update, generate_post_data

URL = "http://localhost:8000/api/users/"
db = requests.get(URL)
response = db.json()
index = 1

for item in response:
    URL_PUSH = f"http://localhost:8000/api/users/{index}/"
    new_data = {}
    for new_keys in ['id','description','photos']:
        new_data[new_keys] = item[new_keys]
    # for condition in ['<p>', '</p>', '<span>', '</span>', '<br>', '<br />']:
    #     if re.search('br', condition):
    #         new_data['description'] = new_data['description'].replace(condition, '\n')
    #     else:
    #         new_data['description'] = new_data['description'].replace(condition, '')
    # regexdata = re.compile('<.*?>')
    # new_data['description'] = re.sub(regexdata, '', new_data['description'])
    resize_photos = []
    for photo in new_data['photos']:
        resize_photos.append(photo.replace('?w=480', ''))
    new_data['photos'] = resize_photos
    updater = requests.patch(URL_PUSH, json=new_data)
    print(updater.text)
    index += 1
