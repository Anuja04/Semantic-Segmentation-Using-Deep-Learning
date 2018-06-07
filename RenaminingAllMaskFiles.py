import os
import PIL

def renameMask(maskPath,newFilename):
    newPath="/Users/anujatike/Documents/sem4/CS256/project/trainData/"+newFilename
    os.rename(maskPath, newPath)

def main():
    #root folder for the resized images directory
    root = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train_resized"
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
                newFilename=filenameArr[0]+"_mask.png"
                print(newFilename)

        if "masks" in dirpath:
            for filename in files:
                if "target" in filename:
                    maskPath=os.path.join(dirpath, filename)
                    print(maskPath)

                    renameMask(maskPath,newFilename)




main()