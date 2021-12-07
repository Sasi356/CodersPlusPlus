import os

from detectron2.data import DatasetCatalog, MetadataCatalog
from data_p import get_data_dicts
from globals import classes

from detectron2 import model_zoo
from detectron2.config import get_cfg

def register_train(path):
    microcontroller_metadata = None
    try:
        DatasetCatalog.register(
            "category_train", 
            lambda func = "train": get_data_dicts(path + "train", classes)
        )
        MetadataCatalog.get("category_train").set(thing_classes = classes)
        microcontroller_metadata = MetadataCatalog.get("category_train")
    except:
        DatasetCatalog.remove("category_train")
        MetadataCatalog.remove("category_train")
        microcontroller_metadata = register_train(path)
    return microcontroller_metadata

def register_valid(path):
    try:
        DatasetCatalog.register(
            "category_valid",
            lambda func = "valid": get_data_dicts(path + "valid", classes) 
        )
    except:
        DatasetCatalog.remove("category_valid")

def get_config():
    return get_cfg()

def config_train(cfg, device = 'cuda', iterations = 1000, lr = 0.00025, ipb = 4):
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
    cfg.DATASETS.TRAIN = ("category_train",)
    cfg.DATASETS.TEST = ()
    cfg.MODEL.DEVICE = device
    cfg.DATALOADER.NUM_WORKERS = 2
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
    cfg.SOLVER.IMS_PER_BATCH = ipb
    cfg.SOLVER.BASE_LR = lr
    cfg.SOLVER.MAX_ITER = iterations
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(classes)
    return cfg

def config_test(cfg, threshold = 0.5):
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold 
    cfg.DATASETS.TEST = ("category_valid", )