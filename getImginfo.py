import requests, json, re
from utils import loadFromJson, saveToJson, readImgSize

# http://127.0.0.1:8080/api/tasks?page=1&page_size=3000&view=5&project=3
img_folder = 'D:\\NTUT\\Lab\\SAM\\civilianvehicle\\civilianvehicle_images'
img_list = loadFromJson('img_list.json')

for img in img_list['tasks']:
    filename = re.search(r'\-(\d+)\.', img['data']['image']).group(1)
    w, h = readImgSize(img_folder + '\\' + filename + '.png')
    print(filename, w, h)
    img['data']['width'] = w
    img['data']['height'] = h
    img['data']['filename'] = filename

saveToJson(img_list, 'img_list.json')
