from ProcessImage import Load_Image, Resize_Image, Detect_box, Save_Image, Process_Image
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

from_path = "/home/ramiz/signatureDetection/Signs/urdu/"
to_path = "/home/ramiz/signatureDetection/Signs/Processed-Original/"

print("Starting operations on urdu signatures")
count = Process_Image(from_path, to_path, "Urdu", 1, first_name="URD_0", extension=".jpg")


print("Completed")