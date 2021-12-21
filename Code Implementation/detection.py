#================================================================
#
#   File name   : detection.py
#   Description : object detection - image or video
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model
from yolov3.configs import *

image_path   = "./Inputs/kite.jpg"
video_path   = "./Inputs/1c.mp4"

yolo = Load_Yolo_model()

#detect_image(yolo, image_path, "./Outputs/kite_pred.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255,0,0))

#detect_video(yolo, video_path, "./Outputs/Output1cnew.mp4", input_size=YOLO_INPUT_SIZE, show=False, rectangle_colors=(255,0,0))

detect_realtime(yolo, "./Outputs/Output.mp4", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255, 0, 0))

