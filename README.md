# basketballVideoAnalysis

See wiki page for [more details](https://github.com/stephanj/basketballVideoAnalysis/wiki).

## Court Detection

ToDo

## Mask R-CNN of persons (mask-rcnn)

First get the frozen inference graph from link below and place this in mask-rcnn/mask-rcnn-coco directory

https://basketball-ml.s3-eu-west-1.amazonaws.com/frozen_inference_graph.pb

Now you can run the Mask RCNN application using following command

```
python mask_rcnn.py -i images/basketball.jpg -m mask-rcnn-coco -v 1
```

Image output example

[<img width="2025" alt="defence" src="https://user-images.githubusercontent.com/179457/70865878-af81d900-1f62-11ea-85d1-44db19a0f7f3.jpg">](https://www.youtube.com/watch?v=yEqGTSd5DQU)

Video output example

https://www.youtube.com/watch?v=yEqGTSd5DQU

The masked image result is placed in the output directory including the segmented image files.

## Color detection of persons (color-detection)

Run the script run.sh to execute color detection on the 25 extracted segments from the Mask R-CNN application.
The resulting colorbar images are stored in the samples directory.

The color detection shows a color map per segmented output from Mask R-CNN.  This is required to do classification of players and link them to a team.

![Colors](https://user-images.githubusercontent.com/179457/71019085-040b8c80-20fa-11ea-8e44-d22759d9352a.jpg)

## Player classification

ToDo 

## Convolutional Pose Machines (CPM) 

ToDo 

Required so we can classify the game play action of players.

## Homography mapping of court

ToDo

Maps the 3D court onto a 2D version, required for analysis of movement.
