# from ProcessImage import Load_Image, Resize_Image,Detect_box, Process_Image
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import cv2

# from_path = "/home/ramiz/signatureDetection/Signs/urdu/Urdu/"

# to_path = "/home/ramiz/signatureDetection/Signs/Processed-Original/Urdu/"

# images = Load_Image(from_path)

# res_img, boxed = [], []
# for i in range(len(images)):
    # res = Resize_Image(images[i])
    # if res is not None:
        # res_img.append(res)

# for i in range(len(res_img)):
    # box = Detect_box(res_img[i])
    # if box is not None:
        # boxed.append(box)



# def Save(path, imagelist):
    # filename = "UDU_"
    # extension = ".jpg"
    # start = 1
    # for i in range(len(imagelist)):
        # to_ad = path + filename + str(start) + extension
        # cv2.imwrite(to_ad, imagelist[i])
        # start += 1

# Save(to_path, boxed)

# print(" COMPLETED")
