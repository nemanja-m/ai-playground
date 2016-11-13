from skimage.io import imread
from skimage.measure import label, regionprops
from skimage.color import rgb2gray
import numpy as np

class ImageUtils:

    #  Extract regions from input image, that
    #  contains MNIST digits. Regions are 28x28 pixels each.

    @staticmethod
    def regions(image_path):
        # Read image and convert it to binary
        image     = imread(image_path)
        grayscale = rgb2gray(image)
        binary    = grayscale > 0

        # Get properites for each region
        properties = regionprops(label(1 - binary))

        regions = []
        for prop in properties:
            height = prop.bbox[2] - prop.bbox[0]
            width  = prop.bbox[3] - prop.bbox[1]

            # If regions have right size
            if (height == 28 and width == 28):
                x = prop.bbox[0]
                y = prop.bbox[1]

                # Crop region from grayscale image
                region = np.zeros((28, 28), np.float)
                region[0:28, 0:28] = grayscale[x:x + 28, y:y + 28] * 255

                regions.append(region)

        return regions


