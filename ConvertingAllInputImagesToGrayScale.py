import os
import numpy as np
from PIL import Image

#Converting images to grayscale
def convertToGrayScale(newFilename,sourceImagePath):
    x = Image.open(sourceImagePath, 'r')
    x = x.convert('L')  # makes it greyscale
    y = np.asarray(x.getdata(), dtype=np.float64).reshape((x.size[1], x.size[0]))

    y = np.asarray(y, dtype=np.uint8)  # if values still in range 0-255!
    w = Image.fromarray(y, mode='L')
    imagePath="/Users/anujatike/Documents/sem4/CS256/project/trainData/"
    actualImage=imagePath+newFilename+".png"
    w.save(actualImage)


def main():

    #Root path to search for "Images" folder in all image folders
    #root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'
    root = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train_resized/"

    #Searching image and mask to resize in images and masks folder respectively
    for dirpath, dirs, files in os.walk(root):

        if "image" in dirpath:
            for filename in files:
                # Path of image file to resize
                sourceImagePath = os.path.join(dirpath, filename)
                #print(sourceImagePath)
                #print(filename)
                filenameArr= filename.split("-")
                #print(filenameArr)

                #This is new filename given to gray scale input image
                newFilename=filenameArr[0]
                #print(newFilename)
                convertToGrayScale(newFilename,sourceImagePath)





main()