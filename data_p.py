import os
import json
from PIL import Image
import shutil
from globals import classes

def correction(path):
    files = os.listdir(path)
    files.sort()
    
    i = 0
    while i < len(files):
        if files[i][:-4] != files[i + 1][:-5]:
            os.remove(path + files[i])
            files.remove(files[i])
        else:
            i += 2
    
def get_data_dicts(directory, classes):
    dataset_dicts = []
    correction(directory)
    for filename in [file for file in os.listdir(directory) if file.endswith('.json')]:
        json_file = os.path.join(directory, filename)
        with open(json_file) as f:
            img_anns = json.load(f)

        record = {}
        
        filename = os.path.join(directory, img_anns["imagePath"])
        
        record["file_name"] = filename
        record["height"] = 500
        record["width"] = 850
      
        annos = img_anns["shapes"]
        objs = []
        for anno in annos:
            px = [a[0] for a in anno['points']] # x coord
            py = [a[1] for a in anno['points']] # y-coord
            poly = [(x, y) for x, y in zip(px, py)] # poly for segmentation
            poly = [p for x in poly for p in x]

            obj = {
                "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                "bbox_mode": BoxMode.XYXY_ABS,
                "segmentation": [poly],
                "category_id": classes.index(anno['label']),
                "iscrowd": 0
            }
            objs.append(obj)
        record["annotations"] = objs
        dataset_dicts.append(record)
    return dataset_dicts

def filters():
    pass