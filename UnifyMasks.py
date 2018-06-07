from PIL import Image
import os
import numpy as np
import scipy.misc as spm


def unifyMasks(dirpath, files):
    targetImagePixels = np.zeros((256, 256), dtype=np.uint8)

    #all masks are combined into a single, unified mask to obtain a target image
    for filename in files:
        sourceImagePath = os.path.join(dirpath, filename)
        sourceImage = Image.open(sourceImagePath)
        sourceImagePixels = sourceImage.load()
        for i in range(0, 256):
            for j in range(0, 256):
                targetImagePixels[i, j] += sourceImagePixels[i, j]

    #without transposition, the target image will be an inverted image
    targetImagePixels = np.matrix.transpose(targetImagePixels)

    #converting array to an image and then saving it
    targetImage = spm.toimage(targetImagePixels)
    targetImagePath = dirpath + "/target.png"
    targetImage.save(targetImagePath)


def main():
    #root folder for the resized images directory
    root = "/Users/anujatike/Documents/sem4/CS256/project/Data/stage1_train_resized"

    #creating a target.png image in each mask folder that represents a combination of all masks for a
    #given image
    for dirpath, dirs, files in os.walk(root):
        if "masks" in dirpath:
            print(dirpath)
            unifyMasks(dirpath, files)


if __name__ == "__main__":
    main()
