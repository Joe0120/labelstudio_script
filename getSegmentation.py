import requests
import json
from utils import loadFromJson, saveToJson
from db_pymongo import insertDB, findByID

url = "http://localhost:8080/api/ml/3/interactive-annotating"

headers = {
  'Accept': '*/*',
  'Cookie': '_ga=GA1.1.659053664.1688443671; csrftoken=V0a77A0tlhA09Co0pPPONGJOrFvTvSaJwpSnsHg1nPTmEu9b7LyWOV2et6sZdrYt; _ga_Z4KXEBY4VP=GS1.1.1688443671.1.0.1688443679.52.0.0; sessionid=.eJxVj81uxCAMhN-F8yYCYv5y7L3PEJlgEroRrEIi9Ud995JqL3vwwTOfZ-QfdqbARqYNASgVuzlG04GVqrPSmM4rFFGRDkCO3VjZF8zpG49U8vS4s1Hc2Ib1mLaypNxWbS3AoI3rtXZykM2f8DzW6ay0T_9Vgr1oHuc75csIH5iX0s8lH3vy_YX0T7f27yXQ9vZkXwJWrGu7ttrMs3BgOQmPfjBKCE5BOgIcdJumkDPaAlfeReMMADXYq2gEBn-FVqr1-ow-H2n_YiMMknP--wfR3FrP:1qHL3P:AfU2vc2J0ffNp87qADqNY7wHk1QFgFerEDmGeXcFPa0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'content-type': 'application/json'
}
img_list = loadFromJson('img_list.json')

for img in img_list['tasks']:
    for label_index, label in enumerate(img['labels']):
        if findByID(img['id']): continue
        print(label['labelstudio'])
        print(f"id: {img['id']}/{img_list['tasks'][-1]['id']}, label: {label_index}/{len(img['labels'])}")
        payload = json.dumps({
            "task": img['id'],
            "context": {
              "result": [
                {
                  "original_width": img['data']['width'],
                  "original_height": img['data']['height'],
                  "image_rotation": 0,
                  "value": {
                    "x": label['labelstudio']['x'],
                    "y": label['labelstudio']['y'],
                    "width": label['labelstudio']['w'],
                    "height": label['labelstudio']['h'],
                    "rotation": 0,
                    "rectanglelabels": [
                      "car"
                    ]
                  },
                  "from_name": "RectangleLabels",
                  "to_name": "image",
                  "type": "rectanglelabels",
                  "origin": "manual"
                }
              ]
            }
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        segmentation = res['data']['result'][1]['value']['rle']
        label['labelstudio']['segmentation'] = segmentation
    # saveToJson(img_list, 'seg.json')
    insertDB(img)

