import json
import cv2

def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def save2YoloFormat(filename, yolo):
    with open(f"labels_seg\\{filename}.txt", "a") as f:        
        for val in yolo:
            f.write("{} {:.6f}".format(1,val))
        f.write("\n")

def loadFromJson(filename):
    with open(filename, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def saveToJson(ls, filename):
    json_object = json.dumps(ls, indent=4, ensure_ascii=False)
    with open(filename, "w", encoding="utf-8") as outfile:
        outfile.write(json_object)

def readImgSize(file):
    im = cv2.imread(file)
    h, w, c = im.shape
    return w, h

def yolo2labelstudio_format(label_arr):
    [type, center_x, center_y, w, h] = label_arr
    # yolo: center_x, center_y, width, height
    # labelstudio: (topleft_x, topleft_y, width, height)*100
    topleft_x = center_x*100-(w*100/2)
    topleft_y = center_y*100-(h*100/2)
    width = w*100
    height = h*100
    return topleft_x, topleft_y, width, height