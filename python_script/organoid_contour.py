# organoid_thresh
# import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
def gray_image():
   pass 


def organoid_contour():
   image = input('Please enter the path to your image here: ')
   img = cv.imread(image)
   img = cv.blur(img, (20,20))


   #kernel = np.ones((5,5),np.float32)/25
   #dst = cv.filter2D(img,-1,kernel)
   assert img is not None, "file could not be read, check with os.path.exists()"
   gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
   ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
   contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


   cnt = contours[0]
   M = cv.moments(cnt) # look at contours in openCV page in the documentation


   #im1 = cv.drawContours(img, contours, -1, (255,255,255), -1)


   mask = np.zeros(img.shape,np.uint8)
   image = cv.drawContours(mask,contours,-1, (255,255,255),-1) 


   return image


def export_contoured_image():
   image = organoid_contour()
   masked_image = cv.imwrite('masked_image.png', image)
   return masked_image


if __name__ == '__main__':
   export_contoured_image()