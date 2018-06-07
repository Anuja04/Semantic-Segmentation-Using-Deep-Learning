from tf_unet import unet, util, image_util
import numpy
import PIL

data_provider = image_util.ImageDataProvider(
        "/Users/anujatike/Documents/sem4/CS256/project/trainData/*",
        data_suffix=".png", mask_suffix="_mask.png")

net = unet.Unet(channels=1, n_class=2, layers=3, features_root=64)
trainer = unet.Trainer(net)
output_path = "output"
path = trainer.train(data_provider, output_path, training_iters=10, epochs=10)  #100)

print(path)

