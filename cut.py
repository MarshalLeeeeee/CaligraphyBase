import cv2
import os
import numpy as np

def cut(path):
	dataPath = os.path.join(path,'raw')
	savePath = os.path.join(path,'cut')
	width = 64
	xHead,yHead = 283,302
	xDelta,yDelta = 173,208
	cnt = 1
	#a,b = 460,510
	#a,b = 285,510
	#a,b = xHead+8*xDelta,510
	for name in os.listdir(dataPath):
		img = cv2.imread(os.path.join(dataPath,name))
		for x in range(11):
			for y in range(6):
				img2 = img[xHead+x*xDelta-width:xHead+x*xDelta+width,yHead+y*yDelta-width:yHead+y*yDelta+width,:]
				cv2.imwrite(os.path.join(savePath,'simp_'+str(cnt)+'.png'),img2)
				cnt += 1

if __name__ == '__main__':
	path = '..\demo\simp'
	cut(path)