from ProcessImage import Load_Image, Resize_Image, Detect_box, Save_Image, Process_Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

<<<<<<< HEAD
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
boxed_22 = resize_box(Hindi_22)
boxed_23 = resize_box(Hindi_23)
boxed_24 = resize_box(Hindi_24)
boxed_25 = resize_box(Hindi_25)
boxed_26 = resize_box(Hindi_26)
boxed_27 = resize_box(Hindi_27)
boxed_28 = resize_box(Hindi_28)
boxed_29 = resize_box(Hindi_29)
boxed_30 = resize_box(Hindi_30)

print("............")
boxed_31 = resize_box(Hindi_31)
boxed_32 = resize_box(Hindi_32)
boxed_33 = resize_box(Hindi_33)
boxed_34 = resize_box(Hindi_34)
boxed_35 = resize_box(Hindi_35)
boxed_36 = resize_box(Hindi_36)
boxed_37 = resize_box(Hindi_37)
boxed_38 = resize_box(Hindi_38)
boxed_39 = resize_box(Hindi_39)
boxed_40 = resize_box(Hindi_40)

print("...........")
boxed_41 = resize_box(Hindi_41)
boxed_42 = resize_box(Hindi_42)
boxed_43 = resize_box(Hindi_43)
boxed_44 = resize_box(Hindi_44)
boxed_45 = resize_box(Hindi_45)
boxed_46 = resize_box(Hindi_46)



print(os.getcwd())
os.chdir("../..")
print(os.getcwd())

print(Hindi_31[5].shape)
print(boxed_31[5].shape)
cv2.imshow("original", Hindi_46[5])
cv2.imshow("boxed", boxed_46[5])

cv2.waitKey()
cv2.destroyAllWindows() 
=======
print("\n\n\n________.............................________\n\n\n")

from_path = "/home/ramiz/signatureDetection/Signs/Originals/Hindi/"
to_path = "/home/ramiz/signatureDetection/Signs/Processed-Original/Hindi/"


count = Process_Image(from_path, to_path, '22', 680, first_name="HIN_0",  extension='.jpg')
print("\n22 completed")
count = Process_Image(from_path, to_path, '23', count, first_name="HIN_0",  extension='.jpg')
print("\n23 completed")
count = Process_Image(from_path, to_path, '24', count, first_name="HIN_0",  extension='.jpg')
print("\n24 completed")
count = Process_Image(from_path, to_path, '25', count, first_name="HIN_0",  extension='.jpg')
print("\n25 completed")
count = Process_Image(from_path, to_path, '26', count, first_name="HIN_0",  extension='.jpg')
print("\n26 completed")
count = Process_Image(from_path, to_path, '27', count, first_name="HIN_0",  extension='.jpg')
print("\n27 completed")
count = Process_Image(from_path, to_path, '28', count, first_name="HIN_0",  extension='.jpg')
print("\n28 completed")
count = Process_Image(from_path, to_path, '29', count, first_name="HIN_0",  extension='.jpg')
print("\n29 completed")
count = Process_Image(from_path, to_path, '30', count, first_name="HIN_0",  extension='.jpg')
print("\n30 completed")


count = Process_Image(from_path, to_path, '31', count, first_name="HIN_0",  extension='.jpg')
print("\n31 completed")
count = Process_Image(from_path, to_path, '32', count, first_name="HIN_0",  extension='.jpg')
print("\n32 completed")
count = Process_Image(from_path, to_path, '33', count, first_name="HIN_0",  extension='.jpg')
print("\n33 completed")
count = Process_Image(from_path, to_path, '34', count, first_name="HIN_0",  extension='.jpg')
print("\n34 completed")
count = Process_Image(from_path, to_path, '35', count, first_name="HIN_0",  extension='.jpg')
print("\n35 completed")
count = Process_Image(from_path, to_path, '36', count, first_name="HIN_0",  extension='.jpg')
print("\n36 completed")
count = Process_Image(from_path, to_path, '37', count, first_name="HIN_0",  extension='.jpg')
print("\n37 completed")
count = Process_Image(from_path, to_path, '38', count, first_name="HIN_0",  extension='.jpg')
print("\n38 completed")
count = Process_Image(from_path, to_path, '39', count, first_name="HIN_0",  extension='.jpg')
print("\n39 completed")
count = Process_Image(from_path, to_path, '40', count, first_name="HIN_0",  extension='.jpg')
print("\n40 completed")


count = Process_Image(from_path, to_path, '41', count, first_name="HIN_0",  extension='.jpg')
print("\n41 completed")
count = Process_Image(from_path, to_path, '42', count, first_name="HIN_0",  extension='.jpg')
print("\n42 completed")
count = Process_Image(from_path, to_path, '43', count, first_name="HIN_0",  extension='.jpg')
print("\n43 completed")
count = Process_Image(from_path, to_path, '44', count, first_name="HIN_0",  extension='.jpg')
print("\n44 completed")
count = Process_Image(from_path, to_path, '45', count, first_name="HIN_0",  extension='.jpg')
print("\n45 completed")
count = Process_Image(from_path, to_path, '46', count, first_name="HIN_0",  extension='.jpg')
print("\n46 completed")


print("|||COMPLETED|||")
>>>>>>> ramiz
