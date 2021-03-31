from ProcessImage import Load_Image, Resize_Image, Detect_box, Process_Image
import os
import cv2
import matplotlib.pyplot as plt

img = plt.imread("/home/ramiz/signatureDetection/jainab_jp.jpeg")
img2 = plt.imread("/home/ramiz/signatureDetection/nasima_jp.jpeg")
imList = [img, img2]



greyList = []
for i in range(len(imList)):
    img = cv2.cvtColor(imList[i], cv2.COLOR_BGR2GRAY)
    if img is not None:
        greyList.append(img)


# def show_image(imageList, i, num_rows=2, num_cols=2, axis_off=True, figsize=(10, 5)):
#     x = 1
#     plt.figure(figsize=figsize)
#     while (x <= num_rows*num_cols):
#         plt.subplot(num_rows, num_cols, x)
#         plt.imshow(imageList[i])
#         if axis_off:
#             plt.axis("off")
#         x+=1
#         i+=1

 # show_image(imList, 0, num_rows=1, num_cols=2, axis_off=False)

 # show_image(greyList, 0, num_rows=1, num_cols=2, axis_off=False)

print(len(imList), len(greyList))
# cv2.imshow("grey image", greyList[0])
cv2.imshow("grey image", greyList[1])

cv2.waitKey()