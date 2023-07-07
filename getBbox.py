import requests, json, re
from utils import loadFromJson, saveToJson, readFile, yolo2labelstudio_format

label_folder = 'D:\\NTUT\\Lab\\SAM\\civilianvehicle\\civilianvehicle_labels'
img_list = loadFromJson('img_list.json')

for img in img_list['tasks']:
    print(img['data']['filename'])
    filename = img['data']['filename']
    labels = readFile(label_folder + '\\' + filename + '.txt')
    img["labels"]=[]
    for label in labels:
        label = [float(e) for e in label.replace("\n", "").split(" ")]
        topleft_x, topleft_y, width, height = yolo2labelstudio_format(label)
        img["labels"].append({
            "labelstudio":{"x":topleft_x,"y":topleft_y,"w":width,"h":height},
            "yolo":{"x":label[1],"y":label[2],"w":label[3],"h":label[4]}
        })
saveToJson(img_list, 'img_list.json')
