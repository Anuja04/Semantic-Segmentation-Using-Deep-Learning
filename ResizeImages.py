from PIL import Image
import os
import numpy as np
import scipy.misc as spm


#resize all images and masks to a uniform size of 256 * 256
def resizeImage(sourceImagePath, filename, targetImageDirPath):
    sourceImage = Image.open(sourceImagePath)
    targetImage = sourceImage.resize((256, 256))
    filename = filename + "-resized.png"
    targetImagePath = targetImageDirPath + filename
    targetImage.save(targetImagePath)


def main():

    #Root path to search for "Images" folder in all image folders
    #root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'
    root = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train"

    #Searching image and mask to resize in images and masks folder respectively
    for dirpath, dirs, files in os.walk(root):

        if "images" in dirpath:
            for filename in files:

                #Path of image file to resize
                sourceImagePath = os.path.join(dirpath, filename)

                #Extracting only name and not extention from filename
                imageNameOnly = filename.split(".")

                #Passing image name (without extension), sourceImagePath, and target image sub-directory path
                #  to resize the image
                #targetImagePath = "/Users/anujatike/Documents/sem4/CS256/project/Data/resizedImages/"
                targetImageDirPath = "/Users/anujatike/Documents/sem4/CS256/project/Data/AllTrainImages/" + imageNameOnly[0]
                targetImageSubDirPath = targetImageDirPath + "/image/"
                if not os.path.exists(targetImageDirPath):
                    os.makedirs(targetImageDirPath)
                if not os.path.exists(targetImageSubDirPath):
                    os.makedirs(targetImageSubDirPath)
                resizeImage(sourceImagePath, imageNameOnly[0], targetImageSubDirPath)

        if "masks" in dirpath:
            for filename in files:

                #Path of mask files to resize
                sourceImagePath = os.path.join(dirpath, filename)

                #Extracting only name and not extention from filename
                maskNameOnly = filename.split(".")

                #extracting name of image, which is the name of the folder above the current one
                imageDirs = dirpath.split("/")
                imageNameTemp = imageDirs[len(imageDirs) - 2]
                #imageNameOnly = imageNameTemp.split("\\")

                #Passing only mask name wihout extension, maskFilePath and resizedMaskPath to resize the mask
                #resizedMaskPath = "/Users/anujatike/Documents/sem4/CS256/project/Data/resizedMasks/"
                targetImageDirPath = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train_resized/" + imageNameTemp
                targetImageSubDirPath = targetImageDirPath + "/masks/"
                if not os.path.exists(targetImageDirPath):
                    os.makedirs(targetImageDirPath)
                if not os.path.exists(targetImageSubDirPath):
                    os.makedirs(targetImageSubDirPath)

                resizeImage(sourceImagePath, maskNameOnly[0], targetImageSubDirPath)


if __name__ == "__main__":
    main()