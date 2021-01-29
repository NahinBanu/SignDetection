from ProcessImage import Load_Image, Resize_Image, Detect_box, Save_Image
import matplotlib.pyplot as plt
import cv2
import os

path = str(input("enter the path of the folder : "))

print("data loading")
english_original = Load_Image(path)
print("complete")
resized_english = []
for i in range(len(english_original)):
    print("|--|")
    img = Resize_Image(english_original[i])
    if img is not None:
        resized_english.append(img)

print("detecting box")
boxed_img = []
for i in range(len(resized_english)):
    print(".....")
    img = Detect_box(resized_english[i], Crop=True)
    if img is not None:
        boxed_img.append(img)

Save_Image(boxed_img)

cv2.imshow("original", english_original[0])
cv2.imshow("resized", resized_english[0])
cv2.imshow("boxed", boxed_img[0])

cv2.waitKey()
cv2.destroyAllWindows()
