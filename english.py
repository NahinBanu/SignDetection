# from ProcessImage import Load_Image, Resize_Image, Detect_box, Save_Image, Process_Image
# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# import os

# from_path = "/home/ramiz/signatureDetection/Signs/Originals/English/"
# to_path = "/home/ramiz/signatureDetection/Signs/Processed-Original/English/"

# English_list = Load_Image(from_path)
# print(len(English_list))

# print("\nOperation started......")
# boxed_img = []
# for i in range(len(English_list)):
# 	image = Resize_Image(English_list[i])
# 	boxxd = Detect_box(image)
# 	if box is not None:
# 		boxed_img.append(boxxd)

# def save_image(imagelist, to_path, name, middle, extension = ".jpg"):
# 	for i in range(len(imagelist)):
# 		path = to_path + name + str(middle) + extension
# 		cv2.imwrite(path, imagelist[i])
# 		middle += 1

# 	return middle

# print("\n Saving ..........")
# count = save_image(boxed_img, to_path, 'ENG_0', 1)

# print(count)

# print("\n\n\n\ncompleted")
