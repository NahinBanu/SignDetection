from ProcessImage import Load_Image, Resize_Image, Detect_box
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

os.chdir("./Signs/Originals/Hindi/")


print("Image Loading.\n")

print("........")
Hindi_01 = Load_Image("./01")
Hindi_02 = Load_Image("./02")
Hindi_03 = Load_Image("./03")
Hindi_04 = Load_Image("./04")
Hindi_05 = Load_Image("./05")
Hindi_06 = Load_Image("./06")
Hindi_07 = Load_Image("./07")
Hindi_08 = Load_Image("./08")
Hindi_09 = Load_Image("./09")
Hindi_10 = Load_Image("./10")

print("........")
Hindi_10 = Load_Image("./10")
Hindi_11 = Load_Image("./11")
Hindi_12 = Load_Image("./12")
Hindi_13 = Load_Image("./13")
Hindi_14 = Load_Image("./14")
Hindi_15 = Load_Image("./15")
Hindi_16 = Load_Image("./16")
Hindi_17 = Load_Image("./17")
Hindi_18 = Load_Image("./18")
Hindi_19 = Load_Image("./19")
Hindi_20 = Load_Image("./20")

print("........")
Hindi_21 = Load_Image("./21")
Hindi_22 = Load_Image("./22")
Hindi_23 = Load_Image("./23")
Hindi_24 = Load_Image("./24")
Hindi_25 = Load_Image("./25")
Hindi_26 = Load_Image("./26")
Hindi_27 = Load_Image("./27")
Hindi_28 = Load_Image("./28")
Hindi_29 = Load_Image("./29")
Hindi_30 = Load_Image("./30")

print("........")
Hindi_31 = Load_Image("./31")
Hindi_32 = Load_Image("./32")
Hindi_33 = Load_Image("./33")
Hindi_34 = Load_Image("./34")
Hindi_35 = Load_Image("./35")
Hindi_36 = Load_Image("./36")
Hindi_37 = Load_Image("./37")
Hindi_38 = Load_Image("./38")
Hindi_39 = Load_Image("./39")
Hindi_40 = Load_Image("./40")

print("........")
Hindi_41 = Load_Image("./41")
Hindi_42 = Load_Image("./42")
Hindi_43 = Load_Image("./43")
Hindi_44 = Load_Image("./44")
Hindi_45 = Load_Image("./45")
Hindi_46 = Load_Image("./46")

print("\nTHE END")

def resize_box(imagelist):
    box_list = []
    for i in range(len(imagelist)):
        img = Resize_Image(imagelist[i])
        image = Detect_box(img, Crop=True)
        if image is not None:
            box_list.append(image)

    return box_list

print("Boxing the images.\n")
print(".........")
boxed_01 = resize_box(Hindi_01)
boxed_02 = resize_box(Hindi_02)
boxed_03 = resize_box(Hindi_03)
boxed_04 = resize_box(Hindi_04)
boxed_05 = resize_box(Hindi_05)
boxed_06 = resize_box(Hindi_06)
boxed_07 = resize_box(Hindi_07)
boxed_08 = resize_box(Hindi_08)
boxed_09 = resize_box(Hindi_09)
boxed_10 = resize_box(Hindi_10)

print("..........")
boxed_11 = resize_box(Hindi_11)
boxed_12 = resize_box(Hindi_12)
boxed_13 = resize_box(Hindi_13)
boxed_14 = resize_box(Hindi_14)
boxed_15 = resize_box(Hindi_15)
boxed_16 = resize_box(Hindi_16)
boxed_17 = resize_box(Hindi_17)
boxed_18 = resize_box(Hindi_18)
boxed_19 = resize_box(Hindi_19)
boxed_20 = resize_box(Hindi_20)

print("...........")
boxed_21 = resize_box(Hindi_21)
boxed_22 = resize_box(Hindi_21)
boxed_23 = resize_box(Hindi_21)
boxed_24 = resize_box(Hindi_21)
boxed_25 = resize_box(Hindi_21)
boxed_26 = resize_box(Hindi_21)
boxed_27 = resize_box(Hindi_21)
boxed_28 = resize_box(Hindi_21)
boxed_29 = resize_box(Hindi_21)
boxed_30 = resize_box(Hindi_31)


print(os.getcwd())
os.chdir("../..")
print(os.getcwd())
os.chdir("./Processed-Original/Hindi")
print(os.getcwd())
# cv2.imshow("original", Hindi_01[5])
# cv2.imshow("boxed", boxed_01[5])
print(os.listdir())
cv2.waitKey()
cv2.destroyAllWindows() 
