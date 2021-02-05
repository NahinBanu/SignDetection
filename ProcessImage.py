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


def Resize_Image(image, dim=(500, 90)):
    """
    This function takes a image and resize the image according to the dimension. And returns the resized image.
    """
    img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return img


def Detect_box(image, Crop = False):
    """
    This function takes a list of image and finds the outer most boundaries.    """
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

    best_box = [-1, -1, -1, -1]
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
        im = image[best_box[1]: best_box[3], best_box[0]: best_box[2]]

    return im

def Save_Image(imagelist, file_add, middle_name, extension):
    """
    This function takes in a list of images and saves it on particular provided directory.
    """
    for i in range(len(imagelist)):
        path = file_add + str(middle_name) + extension
        cv2.imwrite(path, imagelist[i])
        middle_name += 1
    return middle_name


def Process_Image(from_path, to_path, destination, middle_name, first_name='HIN_0', extension=".jpg"):
    """
    This function takes the path of the parent folder and loads images from that folder,
    and also takes the folder address of the folder where new processed images to be saved.

    from_path = path of the folder from where images to be loaded.

    to_path = path where processed to be saved.

    first_name = the common first name of the image files ( default : "HIN_0")

    middle_name = the distint name of the image file.
    
    extension = extension of the image ( default : ".jpg")
    """
    from_add = from_path + destination
    print("Loading Image")
    imagelist = Load_Image(from_add)

    Box_Image, Res_img = [], []
    print("\nResizing Image")
    for i in range(len(imagelist)):
        image = Resize_Image(imagelist[i])
        if image is not None:
            Res_img.append(image)

    for i in range(len(Res_img)):
        box = Detect_box(Res_img[i], Crop=True)
        if box is not None:
            Box_Image.append(box)


    file_add = to_path + destination + "/"+ first_name
    count = Save_Image(Box_Image, file_add, middle_name, extension) 
    print("images saved")

    return count


if __name__ == "__main__":
    Load_Image()
    Resize_Image()
    Detect_box()
    Save_Image()
    Process_Image()


