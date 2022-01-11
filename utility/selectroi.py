#https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/


# import the necessary packages
import argparse
import sys
sys.path.append('/usr/local/python/cv2/python3')
import cv2 as cv

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv.imshow("image", image)

# construct the argument parser and parse the arguments

#fname = 'img/calibimg3.tif'
fname = 'img/img2.tif'

imgori = cv.imread(fname)
height, width = imgori.shape[:2]
image = cv.resize(imgori, (int(width/4), int(height/4)), interpolation = cv.INTER_AREA)

clone = image.copy()
cv.namedWindow("image")
cv.setMouseCallback("image", click_and_crop)

print(''' Select area \n
Keymap :\n
    c   - left click on area and c to print  \n
    r   - reset the cropping region \n
    Esc - exit \n
''')


# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv.imshow("image", image)
	key = cv.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		print('r')
		image = clone.copy()


	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		print('c')
		print('Coordinate:', 	refPt[0][1] * 4,
					refPt[1][1] * 4, 
					refPt[0][0] * 4, 
					refPt[1][0] * 4  )
					
		# if there are two reference points, then crop the region of interest
		# from the image and display it
		'''
		if len(refPt) == 2:
			roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
			cv.imshow("ROI", roi)
			grey = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)  
			cv.imshow('grey ROI',grey)  
			# save image grey
			# status = cv.imwrite('img/grey.jpg',grey)
		'''			
					
		if key == 27:
			print('ESC')
			cv.destroyAllWindows()
			break


# close all open windows
cv.destroyAllWindows()



