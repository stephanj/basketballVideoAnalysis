# USAGE
# python court_detection1.py --input input/kta_court.png
#
# author: Stephan Janssen
#

# import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input image file")
args = vars(ap.parse_args())

# read image from input arg
img = cv2.imread(args["input"])

# convert to HSV image
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# HARD CODED COURT COLOR :(
court_color = np.uint8([[[135,67,72]]])

hsv_court_color = cv2.cvtColor(court_color, cv2.COLOR_BGR2HSV)
hue = hsv_court_color[0][0][0]

# define range of blue color in HSV - Again HARD CODED! :(
lower_color = np.array([hue - 10,10,10])
upper_color = np.array([hue + 10,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv_img, lower_color, upper_color)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

# Show original image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
plt.title('Original Image') 
plt.show()

# Show masked image
plt.imshow(mask, cmap='Greys')
plt.title('Mask')
plt.savefig('output/mask.jpg')
plt.show()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.title("Gray")
plt.show() 

edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
plt.imshow(edges)
plt.title("Edges")
plt.show() 

minLineLength = 100
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
print(lines[0])
print(lines[1])
print(lines[2])
print(lines[3])

# Green color in BGR 
LINE_COLOR = (255, 0, 0) 

for x1, y1, x2, y2 in lines[0]:
    # cv2.line(image, start_point, end_point, color, thickness)
    cv2.line(img, (x1,y1), (x2,y2), LINE_COLOR, 55)

for x1, y1, x2, y2 in lines[1]:
    cv2.line(img, (x1,y1), (x2,y2), LINE_COLOR, 75)

for x1, y1, x2, y2 in lines[2]:
    cv2.line(img, (x1,y1), (x2,y2), LINE_COLOR, 125)

plt.imshow(img)
plt.title('Hough Lines')
plt.show()

# Erosion
kernel = np.ones((2,2),np.uint8)
erosions2 = cv2.erode(mask, kernel, iterations = 5)
plt.imshow(erosions2)
plt.title('Erosions')
plt.show()

# Dilation
dilation = cv2.dilate(mask, kernel, iterations = 3)
plt.imshow(dilation)
plt.title('Dilation')
plt.show()

# Opening
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
plt.imshow(opening)
plt.title('Opening')
plt.show()

# Closing
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing)
plt.title('Closing')
plt.show()
