# Court detection strategies

<img width="548" alt="Courts" src="https://user-images.githubusercontent.com/179457/71198821-f0e0f400-2294-11ea-8253-3d6ff20fcbf9.png">

As you can see in the images above, these are not NBA courts.  Many criss-cross lines define a basketball court which will make it very hard to auto detect.  

Let's have a closer look at a few strategies.  

## Court Detection v1 

* Converting the image to HSV
* Isolating pixels within a given hue range
* Developing a bitwise-AND mask
* Using Canny edge detection
* Using Hough Transformation

<img width="548" alt="Masking" src="https://user-images.githubusercontent.com/179457/71198482-29cc9900-2294-11ea-927b-277d6298a972.png">

The Python code "court_detection1.py" is included in this project.

Basketball court detection (with too many lines) will be very difficult to identify using above strategies.

## Court Detection using binary segmentation using autoencoders v2
An autoencoder for sports field segmentation will be required as explained in the [Classification of Actions](https://www.researchgate.net/publication/330534530_Classificazione_di_Azioni_Cestistiche_mediante_Tecniche_di_Deep_Learning)  by Simone Francia (see section 3.2.2 : Autoencoder model of the basketball court)

<img width="853" alt="court" src="https://user-images.githubusercontent.com/179457/71194460-3b11a780-228c-11ea-8463-4dc84c2b4e5a.png">

### Field Segmentation Datasets

In order for training to work, a 100,000-frame dataset of basketball courts is required.
To do this, about 1000 frames needs to be extracted from each game which is then used for the creation of the data set. 
The size of the dataset can be increased through simple data augmentation techniques.

<img width="541" alt="CourtMarkers" src="https://user-images.githubusercontent.com/179457/71196279-07d11780-2290-11ea-87d7-63d342130ddd.png">

>Through the OpenCV function cv2.polylines it is possible to create n points {p1, p2, .., pn } on the image plane. These points are then used to draw a polygon. 

```python
def draw_poly_box(frame, pts, color=[0, 255, 0]):
    """Draw polylines bounding box.

    Parameters
    ----------
    frame : OpenCV Mat
        A given frame with an object
    pts : numpy array
        consists of bounding box information with size (n points, 2)
    color : list
        color of the bounding box, the default is green

    Returns
    -------
    new_frame : OpenCV Mat
        A frame with given bounding box.
    """
    new_frame = frame.copy()
    temp_pts = np.array(pts, np.int32)
    temp_pts = temp_pts.reshape((-1, 1, 2))
    cv2.polylines(new_frame, [temp_pts], True, color, thickness=2)

    return new_frame
```

This polygon, annotated by manually, is interpreted as a field (basketball court) and colored white inside, while the outside will be black.

<img width="555" alt="BlackWhiteCourt" src="https://user-images.githubusercontent.com/179457/71196872-a8bfd280-2290-11ea-97f5-f6fc4beedea6.png">

### Data Augmentation for the Dataset Field

> The annotation of the field has been carried out for one frame every second, and being the videos of 25 fps, it is equivalent to annotating a frame every 25. The annotation of 1000 frames is not sufficient to create a robust auto-coder model; for this reason, some Data Augmentation solutions have been adopted in order to provide the autoencoder model with a sufficient number of examples for training.

Every court image can also be rotated with an angle ranging from -15 and 15. From each original court image two other combinations are created, choosing a random angle between the interval. 

<img width="566" alt="rotated" src="https://user-images.githubusercontent.com/179457/71199270-e3783980-2295-11ea-92f6-552c7277afea.png">
