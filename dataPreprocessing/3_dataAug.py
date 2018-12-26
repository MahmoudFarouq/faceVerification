import os
from PIL import Image
import numpy as np
from keras.preprocessing.image import ImageDataGenerator


def generate(images, save_dir, aug_scale):
    if generate.gen == None:
        generate.gen = ImageDataGenerator(
                    featurewise_center=True,
                    featurewise_std_normalization=True,
                    rotation_range=20,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    horizontal_flip=True)
        generate.gen.fit(images)
    for x, val in zip(generate.gen.flow(images, save_to_dir=save_dir, save_prefix='aug', save_format='png'), range(aug_scale)):
        pass


def augment(from_folder, to_folder, aug_scale, size=(200, 200)):
    if(not os.path.exists(to_folder)):
        os.mkdir(to_folder)
    path_content = os.listdir(from_folder)
    images_paths = []
    for element in path_content:
        if(os.path.isdir(element)):
            augment( os.path.join(from_folder, element) , os.path.join(to_folder, element))
        else:
            images_paths.append(os.path.join(from_folder, element))
    images = []
    for image_path in images_paths:
        images.append( np.array(Image.open(image_path).resize(size, Image.ANTIALIAS))[:,:,0:3] )
    generate(np.vstack(images).reshape(len(images), size[0], size[1], 3), to_folder, aug_scale)




def main():
	images_path = '/home/sorcerer/Downloads/mlProject/dataSet/omar' 
	save_path = '/home/sorcerer/Downloads/mlProject/dataSet/aug_omar'
	generate.gen = None
	x = augment(images_path, save_path, 10)


if __name__ == '__main__':
	main()