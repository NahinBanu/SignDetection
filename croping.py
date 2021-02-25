from ProcessImage import Load_Image, Resize_Image, Process_Image, Detect_box

from_path = "/home/ramiz/signatureDetection/Signs/Originals/"
to_path = "/home/ramiz/signatureDetection/Signs/Processed-Original"
count = Process_Image(from_path, to_path, "Bangla", 1, first_name="BNG_")