"""
	src: https://github.com/MinaYousryGhattas/face_cropper
"""

from PIL import Image
import os
import sys


directory = '/home/sorcerer/Downloads/mlProject/dataSet/omar'

for file_name in os.listdir(directory):
	print("Processing %s" % file_name)
	image_path = os.path.join(directory, file_name)
	image = Image.open(image_path)
	new_dimensions = (48, 48)
	output = image.resize(new_dimensions, Image.ANTIALIAS)
	os.remove(image_path)
	output.save(image_path, "PNG", quality = 95)
print("All done")
