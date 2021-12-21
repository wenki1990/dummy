<h3>Object Detection using Pre-trained YOLOv3</h3>

<em>Note: Due to meagre computing resource, pre-trained model has been used for this project</em>

<center><img src="readme_images/1.png" width = 800 height = 350></center><p style="text-align:center;"><strong>Overall Architecture of YOLOv3</strong></p><p style="text-align:right;"><a href="https://pylessons.com/YOLOv3-TF2-introduction/"><em>Image Source</em></a></p>

- Pre-trained model weights are used to detect the objects. These weights were obtained by training the YOLO system on the MSCOCO dataset.
- The COCO dataset classes for object detection and tracking include the following pre-trained 80 objects:

```
'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis','snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
```

- To obtain object detections, place your image or video in the ```IMAGES``` directory.
- Modify ```image_path``` or ```video_path``` accordingly in the ```detection.py``` file. Also give appropriate name for the output file.
- Run ```detection.py```

- Please check ```requirments.txt``` for the requisite packages.

<h4>Description of directories and files</h4>

```Inputs``

- Contains input images or videos

```Outputs``

- Contains output images or videos

```model_data```

- Contains pre-trained weights as well as COCO dataset labels

```readme_images``

- Contains images used in the ```README.md`` file

```yolov3```

- ```configs.py```: Configuration file for this project
- ```yolo_versions.py```: Contains main functions for different versions of YOLO algorithm
- ```utils.py```: Contains additional functions for running the YOLO algorithm

```detection.py```

- Run this file to obtain object detections.

*References:*

*1. https://pylessons.com/YOLOv3-TF2-introduction/*

[Go to top](#top)