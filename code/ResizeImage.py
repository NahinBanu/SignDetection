import matplotlib.pyplot as plt
import numpy as np
import cv2
def Resize_Image(image, dim = (224, 224)):
    """
    This function accepts an image and resizes it to provided dimension.
    DEFAULT :
    dim = (224, 224)
    """
    img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return img

if __name__ == "__main__":
    Resize_Image()

