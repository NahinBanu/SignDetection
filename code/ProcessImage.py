import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def Load_Image(path):
    """
    This function takes in the path of the folder and read the images in the folder and returns a image list.
    """
    images = []
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        image = plt.imread(file)
        if image is not None:
            images.append(image)

    return images


def Resize_Image(image, dim=(127, 127)):
    """
    This function takes a image and resize the image according to the dimension. And returns the resized image.
    """
    img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return img


def Detect_box(image, Crop = False):
    """
    This function takes a list of image and finds the outer most boundaries.
    """
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_y = np.zeros(img_yuv.shape[0:2], np.uint8)
    img_y[:, :] = img_yuv[:, :, 0]

    img_blur = cv2.GaussianBlur(img_y, (5,5), 0)
    edges = cv2.Canny(img_blur, 100, 500, apertureSize=3)

    contours, hier = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_area = image.shape[1] * image.shape[0]

    new_contours = []
    for c in contours:
        if cv2.contourArea(c) < img_area:
            new_contours.append(c)

    best_box = []
    for c in new_contours:
        x, y, w, h = cv2.boundingRect(c)
        if best_box[0] < 0:
            best_box = [x, y, x+w, y+h]
        else:
            if x < best_box[0]:
                best_box[0] = x
            if y < best_box[1]:
                best_box[1] = y
            if x+w > best_box[2]:
                best_box[2] = x+w
            if y+h > best_box[3]:
                best_box[3] = y+h

    point_a = (best_box[0], best_box[1])
    point_b = (best_box[2], best_box[3])

    if Crop:
        print("|_|")
        img = image[best_box[1]: best_box[3], best_box[0]: best_box[2]]

    return img

def Save_Image(imagelist):
    """
    This function takes in a list of images and saves it on particular provided directory.
    """
    where_to = str(input("\nEnter the path where the image to be saved : " ))
    os.chdir(where_to)
    name = str(input("Enter the name of the first picture : "))
    extension = str(input("\nEnter the file extension (.jpg/.png) : "))
    for i in range(len(imagelist)):
        fname = name + str(i+1) + extension
        plt.imsave(fname, imagelist[i])


if __name__ == "__main__":
    Load_Image()
    Resize_Image()
    Detect_box()
    Save_Image()


