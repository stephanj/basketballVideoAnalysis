import cv2
import numpy as np
from scipy import ndimage as ndi
from skimage import morphology, filters

class PreProcessImage:

    def __init__(self, image_path):

        self.image = cv2.imread(image_path)


    def resize(self):

        self.resized_img = cv2.resize(self.image, (200,200))
        # self.resized_img = self.image
        return self.resized_img

    def segmentation(self):

        # BGR --> GRAY
        image = cv2.cvtColor(self.resized_img,
                             cv2.COLOR_BGR2GRAY)

        # Negation
        neg_img = 255-image
        im = neg_img.astype('int32')

        # Sobel Operator
        sobel = filters.sobel(im)
        blurred = filters.gaussian(sobel, sigma=1.0)

        # masking of image using watershed tranformation
        light_spots = np.array((image > 150).nonzero()).T
        dark_spots = np.array((image < 5).nonzero()).T
        bool_mask = np.zeros(image.shape, dtype=np.bool)
        bool_mask[tuple(light_spots.T)] = True
        bool_mask[tuple(dark_spots.T)] = True
        seed_mask, num_seeds = ndi.label(bool_mask)

        ws = morphology.watershed(blurred, seed_mask)
        background = max(set(ws.ravel()),
                         key=lambda g: np.sum(ws == g))
        background_mask = (ws == background)
        self.resized_img[background_mask] = 0
        self.img = cv2.cvtColor(self.resized_img,
                                cv2.COLOR_BGR2RGB)
        cv2.imwrite('sobel.jpg', self.img)
        return self.img

    def removebg(self):

        src = self.img
        tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255,
                                 cv2.THRESH_BINARY)
        b, g, r = cv2.split(src)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)

        return dst

