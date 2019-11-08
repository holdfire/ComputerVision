import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input

class CNN:
	def __init__(self, image_path):
		self.image = cv2.imread(image_path)
		self.MobileNet = MobileNet
		self.preprocess_input = preprocess_input
		self.target_size = (224,224)
		self.batch_size = 64

	def cnn_feature(self):
		self.model = self.MobileNet(input_shape = (224,224,3),
									include_top = False, pooling = 'avg')
		image_pp = self.preprocess_input(self.image)
		image_pp = np.array(image_pp)[np.newaxis, :]
		return self.model.predict(image_pp)
