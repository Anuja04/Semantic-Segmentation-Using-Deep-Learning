from tf_unet import unet

import os
import numpy as np
from PIL import Image
import PIL

import numpy

root="/Users/anujatike/Documents/sem4/CS256/project/testDataProcessed/"
net = unet.Unet(channels=1, n_class=2, layers=3, features_root=64)

filelist=[]

for dirpath, dirs, files in os.walk(root):
        for filename in files:
            sourceImagePath = os.path.join(dirpath, filename)
            print(sourceImagePath)
            filelist.append(sourceImagePath)

print(filelist)


for fname in filelist:
    #Extracting only name from fname to give to prediction file
    fnameArr = fname.split("/")
    #fnameArrOnlyName = fnameArr[5].split(".")
    fnameArrOnlyName = fnameArr[8].split(".")

    #Making prediction for each test file
    test_image=numpy.asarray(PIL.Image.open(fname))
    test_image=test_image.reshape(1,256, 256,1)
    prediction = net.predict("output/model.ckpt", test_image)
    output = prediction[0, :, :, 1] * 1000 # Times 1000 because it is hardly visible otherwise
    img = PIL.Image.fromarray(output)
    #img.save('/Users/anujatike/Desktop/outputSampleDiceCoeff/prediction%s.png'%fnameArrOnlyName[0])
    if img!='RGB':
        new_p = img.convert('RGB')
        new_p.save('/Users/anujatike/Desktop/LR01/prediction%s.png'%fnameArrOnlyName[0])

