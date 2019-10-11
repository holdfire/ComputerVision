import cv2
import os
import time

class video2Images:
	def __init__(self, video_path):
		self.video_path = video_path
		self.images_from_video = os.path.join(os.path.dirname(video_path), 'images_from_video')
		if not os.path.exists(self.images_from_video):
			os.makedirs(self.images_from_video)

	def toImages(self, frame_interval = 3, resize = False, new_size = (128,128)):
		video = cv2.VideoCapture(self.video_path)
		count = 0
		rval = video.isOpened()
		# read the video by frames
		while rval:
			count = count + 1
			rval, frame = video.read()
			if count % frame_interval != 0:
				continue
			if rval:
				image = frame
			if resize:
				image = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)
			image_path = os.path.join(self.images_from_video, os.path.basename(self.video_path) + "_" + str(count) + ".jpg")
			cv2.imwrite(image_path, image)
		return self.images_from_video

if __name__ == '__main__':
	# STEP1: process the video to produce pictures
	time_start = time.perf_counter()
	video_path = ""
	obj_video = video2Images(video_path)
	video_images_dir = obj_video.toImages()
	# video_images_dir = os.path.join(os.path.dirname(video_path), "images_from_video")
	time_end1 = time.perf_counter()
	print("STEP 1: It cost %d s to frame the video !" % (time_end1 - time_start))



