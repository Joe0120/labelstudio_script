import numpy as np
from rle2mask import rle_to_mask
from utils import save2YoloFormat
from db_pymongo import get_all_data
data_ls = get_all_data()
print(data_ls)
for data_index, data in enumerate(data_ls):
    filename = data['data']['filename']
    original_width = data['data']['width']
    original_height = data['data']['height']
    for label_index, label in enumerate(data['labels']):
        print(f"id: {data_index+1}/3000, label: {label_index+1}/{len(data['labels'])}")
        
        rle = label['labelstudio']['segmentation']
        image = rle_to_mask(rle,original_height, original_width)

        indices = np.where(image == 255)
        row_indices = indices[0]
        col_indices = indices[1]


        mask = np.column_stack((col_indices, row_indices))
        mask_norm = mask / np.array([original_width, original_height])
        yolo = mask_norm.reshape(-1)

        save2YoloFormat(filename, yolo)

