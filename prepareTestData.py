from PIL import Image
import os
import numpy as np
import scipy.misc as spm


#resize all images and masks to a uniform size of 256 * 256
def resizeImage(sourceImagePath, filename, targetImageDirPath):
    print(filename)
    sourceImage = Image.open(sourceImagePath)
    targetImage = sourceImage.resize((256, 256))
    filename = filename + ".png"
    targetImagePath = targetImageDirPath + filename
    targetImage.save(targetImagePath)

    convertToGrayScale(filename, targetImagePath)


#Converting images to grayscale
def convertToGrayScale(newFilename,sourceImagePath):
    x = Image.open(sourceImagePath, 'r')
    x = x.convert('L')  # makes it greyscale
    y = np.asarray(x.getdata(), dtype=np.float64).reshape((x.size[1], x.size[0]))

    y = np.asarray(y, dtype=np.uint8)  # if values still in range 0-255!
    w = Image.fromarray(y, mode='L')
    imagePath="/Users/anujatike/Documents/sem4/CS256/project/testDataProcessed/"
    actualImage=imagePath+newFilename
    w.save(actualImage)



def main():

    #Root path to search for "Images" folder in all image folders
    #root='/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train'
    root = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_test"

    #Searching image and mask to resize in images and masks folder respectively
    for dirpath, dirs, files in os.walk(root):

        if "images" in dirpath:
            for filename in files:

                #Path of image file to resize
                sourceImagePath = os.path.join(dirpath, filename)
                print(sourceImagePath)
                print(filename)
                #Extracting only name and not extention from filename
                imageNameOnly = filename.split(".")
                print(imageNameOnly[0])

                #Passing image name (without extension), sourceImagePath, and target image sub-directory path
                #  to resize the image
                #targetImagePath = "/Users/anujatike/Documents/sem4/CS256/project/Data/resizedImages/"
                targetImageDirPath = "/Users/anujatike/Documents/sem4/CS256/project/testData/"
                resizeImage(sourceImagePath, imageNameOnly[0], targetImageDirPath)



if __name__ == "__main__":
    main()