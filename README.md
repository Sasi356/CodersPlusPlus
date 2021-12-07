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
   ***Note: Make sure Detectron2 and Pytorch versions are compatible***.
   
   For more details about installation and tutorials of Detectron2 refer [Documentation](https://detectron2.readthedocs.io/en/latest/notes/benchmarks.html)
   
   ### Flow of instance segmentation using Detectron2
   ```
   Detectron2
   |_data        <- dataset handlers and data loaders and registering data
   |_config      <- default configs and handlers
   |_model_zoo   <- pre-trained model links and handler - COCO Instance segmentation model
   |_modeling   
      |_Aarchitecture <- base model and architecture - MRCNN
      |_backbone  <- backbone network - ResNet, FPN
      |_proposal_generator <- region proposal network
      |_roi_heads <- head networks for pooled ROIs - box, mask heads
      |_iteration  <- no. of iteration of training
   |_engine      <- predictor and trainer engines
   |_structures   <- structure classes - Boxes, Instances
   |_utils        <- utility modules - visualizer
   ```
   At last Grids cells are identified on which objects of different classes are falled.
   **Here is the attachment of project notebook:**
   [Advanced Object identification in images](https://colab.research.google.com/drive/138jpOo-iL-G_cFU3pcSfibSyThsMMtiR?authuser=1#scrollTo=LzF18vui2Mku)
   
   ### Mask-RCNN
   Mask R-CNN was built on top of Faster R-CNN with extra feature which is masking the detected objects along with bounding box and predicting the class of object identified. The additional mask output is distinct from the class and box outputs, requiring the extraction of a much finer spatial layout of an object.
   Mask R-CNN and works by adding a branch for predicting an object mask (Region of Interest) in parallel with the existing branch for bounding box recognition in Faster-RCNN.
   #### Mask-RCNN Model:
   ![image](https://user-images.githubusercontent.com/86351798/144879480-95d94a35-391e-4ea7-bd3c-5a0a368c5fb6.png)
   
   Source:[Research Gate](https://www.researchgate.net/figure/Architecture-of-Mask-R-CNN-for-instance-segmentation-on-visualization-technique-images_fig2_351426881)
    
    Input Image -> Resnet(Backbone)-FPN(Feature Pyramid Network) -> RPN(Region Proposal Network) -> ROI(Region of interest) Allignment -> Output(class, Bounding Box and Mask detection)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
> Users Can get started with understanding the basic deep learning techniques like CNNs and exploring different object detection models.
> Understading the documentation of the platform going to be used is crux of any project.



   
