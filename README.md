# Sports Video Analysis

See wiki page for [more details](https://github.com/stephanj/basketballVideoAnalysis/wiki).

## Court Detection

<img width="548" alt="Courts" src="https://user-images.githubusercontent.com/179457/71198821-f0e0f400-2294-11ea-8253-3d6ff20fcbf9.png">

See details on court detection [here](https://github.com/stephanj/basketballVideoAnalysis/tree/master/court-detection).

## Mask R-CNN of persons (mask-rcnn)

See details [here](https://github.com/stephanj/basketballVideoAnalysis/tree/master/mask-rcnn) including online tutorial.

[<img width="2025" alt="defence" src="https://user-images.githubusercontent.com/179457/70865878-af81d900-1f62-11ea-85d1-44db19a0f7f3.jpg">](https://www.youtube.com/watch?v=yEqGTSd5DQU)

Video output example

https://www.youtube.com/watch?v=yEqGTSd5DQU

## Color detection of persons (color-detection)

Run the script run.sh to execute color detection on the 25 extracted segments from the Mask R-CNN application.
The resulting colorbar images are stored in the samples directory.

The color detection shows a color map per segmented output from Mask R-CNN.  This is required to do classification of players and link them to a team.

![Colors](https://user-images.githubusercontent.com/179457/71019085-040b8c80-20fa-11ea-8e44-d22759d9352a.jpg)

## Player classification

ToDo 

## Convolutional Pose Machines (CPM) 

![PoseDetection](https://user-images.githubusercontent.com/179457/71200350-23d8b700-2298-11ea-85eb-37b2c8d07b76.png)

Required so we can classify the game play action of players.

## Homography mapping of court

Maps the 3D court onto a 2D version, required for analysis of movement.

![homography](https://user-images.githubusercontent.com/179457/71249581-d0a94780-231d-11ea-9a4c-4382b6755e3f.jpg)

See details [here](https://github.com/stephanj/basketballVideoAnalysis/tree/master/homography-mapping)
and tutorial [here](https://github.com/stephanj/basketballVideoAnalysis/tree/master/mini-map-tutorial)

