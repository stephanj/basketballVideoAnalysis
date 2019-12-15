# -*- coding: utf-8 -*-
import pycolor
import preProcess
from os.path import abspath, dirname, exists, join
import os
import sys
import cv2
import csv
import timeit
import pandas as pd
import numpy as np
import base64


class ColorDetect:
    """"""
    def __init__(self):
        
        # self.img = cv2.imread(**kwargs)
        pass
    
    def predict(self, image_path):

        preprocess = preProcess.PreProcessImage(image_path)
        preprocess.resize()
        segmented_img = preprocess.segmentation()
        detect = pycolor.ColorDetect(segmented_img, image_path)
        output = detect.detect_color()

        return output



obj = ColorDetect()
print(obj.predict(sys.argv[1]))


