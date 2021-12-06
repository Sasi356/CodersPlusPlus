# Coders++
# -----Advanced Object Identification in Images-----

## About the project:
   In this project we have performed the object detection and instance segmentation of an object using **MRCNN(MASK-REGIONAL CONVOLUTIONAL NEURAL NETWORK)** deep learning technique **DETECTRON2** platform and and also performed identification of grid of images(cells) in which the object was spread. The object to be identified belongs to one of the categories: (1) Vehicles such as cars and motorcycles, (2) Road signage such as zebra crossings and traffic lights, and (3) Structures such as bridges and buildings etc.
   
## DETECTRON2 and MRCNN(MASK-REGIONAL CONVOLUTIONAL NEURAL NETWORK)
   ### DETECTRON2
   Detectron2 is one of the most popular open source library and API developed at Facebook's AI research wing which provides state-of-the-art detection and segmentation algorithms such as semantic, instance segmentations etc., including DensePose, panoptic feature pyramid networks, and numerous variants of the pioneering Mask R-CNN model family. Its extensible design makes it easy to implement cutting-edge research projects without having to fork the entire codebase.
   
   ![image](https://user-images.githubusercontent.com/86351798/144848471-4662edfe-32ba-4f8c-baac-a0bbbd4af9ae.png)
   
   ***Source: [Detectron2](https://ai.facebook.com/blog/-detectron2-a-pytorch-based-modular-object-detection-library-/)***
   #### Detectron2 Installation for your Computer Vision projects
      !pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
      !pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html
   ***Note: Make sure Detectron2 and Pytorch versions are compatible***
   For more details about installation and tutorials of Detectron2 refer [Documentation](https://detectron2.readthedocs.io/en/latest/notes/benchmarks.html)
   
   ### Flow of instance segmentation using Detectron2
   ```
   Detectron2
   ├─data        <- dataset handlers and data loaders and registering data
   ├─config      <- default configs and handlers
   ├─model_zoo   <- pre-trained model links and handler - COCO Instance segmentation model
   ├─modeling   
      ├─meta_arch <- meta architecture - MRCNN
      ├─backbone  <- backbone network - ResNet, FPN
      ├─proposal_generator <- region proposal network
      └─roi_heads <- head networks for pooled ROIs - box, mask heads
   ├─engine      <- predictor and trainer engines
   ├─structures   <- structure classes - Boxes, Instances
   └─utils        <- utility modules - visualizer
   ```
   ## Mask-RCNN
   
Why the project is useful
How users can get started with the project
Where users can get help with your project
Who maintains and contributes to the project



   
