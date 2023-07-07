from labelstudio_api import getImg_info, delete_ann, delete_draft, add_ann
from utils import loadFromJson, saveToJson
from db_pymongo import get_all_data
import json

img_list = get_all_data()

for img in img_list:
    print(img['id'])
    result = []
    _index = 0
    for label_index, label in enumerate(img['labels']):
        label_obj= {
            "original_width": img['data']['width'],
            "original_height": img['data']['height'],
            "image_rotation": 0,
            "value": {
                "x": label['labelstudio']['x'],
                "y": label['labelstudio']['y'],
                "width": label['labelstudio']['w'],
                "height": label['labelstudio']['h'],
                "rotation": 0,
                "rectanglelabels": ["car"]
            },
            "id": _index,
            "from_name": "RectangleLabels",
            "to_name": "image",
            "type": "rectanglelabels",
            "origin": "manual"
        }
        _index+=1
        label_ann = {
            "original_width": img['data']['width'],
            "original_height": img['data']['height'],
            "image_rotation": 0,
            "value": {
                "format": "rle",
                "rle": label['labelstudio']['segmentation'],
                "brushlabels": ["car"]
            },
            "id": _index,
            "from_name": "BrushLabels",
            "to_name": "image",
            "type": "brushlabels",
            "origin": "manual"
        }
        result.append(label_obj)
        result.append(label_ann)
    res = add_ann(img['id'], result)
    
    print(res.status_code)
    # print(res.text)
    # print(result)