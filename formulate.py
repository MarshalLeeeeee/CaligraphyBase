import cv2
import os
import numpy as np
from PIL import Image

if __name__ == '__main__':
	img = cv2.imread('..\demo\wangxizhi\yi-0-0.png')
	print(img.shape)
	img2 = img[:378,:,:]
	img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
	_,img2 = cv2.threshold(img2,120,255,cv2.THRESH_BINARY)
	cv2.imwrite('..\demo\wangxizhi\yi-0-0.png',img2)