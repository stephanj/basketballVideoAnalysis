# Notebook Tutorial

* Surf to https://colab.research.google.com/notebooks/welcome.ipynb
* Open Python notebook file : [Basketball_Mask_RCNN.ipynb](Basketball_Mask_RCNN.ipynb)
* Run tutorial step-by-step

# Local Installation

First get the frozen inference graph from link below and place this in mask-rcnn/mask-rcnn-coco directory
https://basketball-ml.s3-eu-west-1.amazonaws.com/frozen_inference_graph.pb

```
pip3 install -r requirements.txt
```

Or mannualy add the following python modules manually

```
numpy==1.17.4
opencv-contrib-python==4.1.2.30
imutils==0.5.3
```

Now you can run the Mask RCNN application using following command

# MASK R-CNN on image 

```
python mask_rcnn.py -i images/basketball.jpg -m mask-rcnn-coco -v 1
```

The masked image result is placed in the output directory including the segmented image files.

# MASK R-CNN on video

```
python mask_rcnn_video.py -i videos/basketball.mp4 -m mask-rcnn-coco

[INFO] loading Mask R-CNN from disk...
[INFO] 235 total frames in video
[INFO] single frame took 1.1975 seconds
[INFO] estimated total time to finish: 281.4151
```

The masked video result is placed in the output directory named output.mp4 
