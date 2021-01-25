import matplotlib.pyplot as plt
import os

def Load_Image(path):
    """
    This function takes the path of the folder and loads the all the files in that folder.
    """
    files = []
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        img = plt.imread(file)
        if img is not None:
            files.append(img)
    return files

if __name__ == "__main__":
    Load_Image()
