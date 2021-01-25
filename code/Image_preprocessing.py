import cv2 as cv
import numpy as np
import os


def Load_Image(path):
    """
    This function takes a path of a folder and returns a list of images in from that folder
    path = path of the folder.
    """
    print("Image Loading began ...")
    ImageList = []
    for fname in os.listdir(path):
        img = cv.imread(os.path.join(path, fname))
        imgg = img / 255
        if img is not None:
            ImageList.append(img)
    print("Image Loading Ended !!")
    return ImageList


def Resize_Image(Image, scale=0.75):
    """
    This function takes a list of image and scales down to its 75% percent mark
    """
    width = int(Image.shape[1] * scale)
    height = int(Image.shape[0] * scale)
    dim = (width, height)
    img = cv.resize(Image, dim, cv.INTER_AREA)
    return img


def Detect_box(Image, CropIt=False):
    """
    This function takes a list of image and finds the outer most boundaries. 
    """
    print("Detecting the boxes")
    img_yuv = cv.cvtColor(Image, cv.COLOR_BGR2YUV)
    img_y = np.zeros(img_yuv.shape[0:2], np.uint8)
    img_y[:, :] = img_yuv[:, :, 0]

    img_blur = cv.GaussianBlur(img_y, (5, 5), 0)

    edges = cv.Canny(img_blur, 100, 500, apertureSize=3)

    contours, heir = cv.findContours(
        edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    img_area = Image.shape[1] * Image.shape[0]

    new_contours = []
    for c in contours:
        if cv.contourArea(c) < img_area:
            new_contours.append(c)

    best_box = [-1, -1, -1, -1]
    for c in new_contours:
        x, y, w, h = cv.boundingRect(c)
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
    if CropIt:
        print("croping ..... ")
        image = Image[best_box[1]: best_box[3], best_box[0]:best_box[2]]
    return image


def save_image(ImageList):
    """
    This function takes an image and saves those images into a directory of your choice.
    """
    where_to = str(input("\nEnter the path : "))
    os.chdir(where_to)
    name = str(input("Enter the first name for images : "))
    for i in range(len(ImageList)):
        fname = name + str(i+1) + ".jpeg"
        cv.imwrite(fname, ImageList[i])


if __name__ == "__main__":
    path = str(input("Enter the path from where images to be read : "))
    Original_Image = Load_Image(path)


    Res_image = []
    for i in range(len(Original_Image)):
        img = Resize_Image(Original_Image[i])
        if img is not None:
            Res_image.append(img)

    Crop_Image = []
    for i in range(len(Res_image)):
        img = Detect_box(Res_image[i], CropIt=True)
        if img is not None:
            Crop_Image.append(img)

    # save_image(Crop_Image)
    cv.imshow("Original Image", Original_Image[500])
    cv.imshow("Resized Image", Res_image[500])
    cv.imshow("Cropped Image", Crop_Image[500])

    cv.waitKey()
    cv.destroyAllWindows()

