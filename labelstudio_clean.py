from labelstudio_api import getImg_info, delete_ann, delete_draft
from utils import loadFromJson, saveToJson

img_list = loadFromJson('img_list.json')

for img in img_list['tasks']:
    print(img['id'])
    res = getImg_info(img['id'])
    if res.status_code != 200: continue
    res = res.json()
    if len(res['drafts']): 
        print(res['drafts'][0]['id'])
        delete_draft(res['drafts'][0]['id'])
    if res['annotations_ids']: 
        print(res['annotations_ids'])
        delete_ann(img['id'], res['annotations_ids'])