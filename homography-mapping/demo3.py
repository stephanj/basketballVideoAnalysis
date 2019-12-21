#
# Author Stephan Janssen
#
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('images/3DbeachVolleyMiddleView.jpg')

# Four corners of the 3D court
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_src = np.array([
    [79, 124],      # 1) top left bottom corner
    [702, 126],     # 2) top right corner
    [798, 201],     # 3) bottom right (bottom part)
    [798, 271],     # 4) bottom right (top part)
    [0, 268],       # 5) bottom left (bottom part)
    [0, 182]        # 6) bottom left (top part)
    ])   

cv2.polylines(img_src, [pts_src], isClosed=True, color=[255,0,0], thickness=2)

plt.imshow(img_src)
plt.title('Original')
plt.show()

# Read destination image.
img_dst = cv2.imread('images/2DBeachVolleyball.jpg')

# Four corners of the court + mid-court circle point in destination image 
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_dst = np.array([
    [26, 131],      # 1) top left bottom corner
    [234, 130],     # 2) top right corner
    [256, 94],      # 3) bottom right (bottom part)
    [256, 6],       # 4) top right corner
    [6, 6],         # 5) top left corner
    [7, 99]         # 6) bottom left corner
    ])   

cv2.polylines(img_dst, [pts_dst], isClosed=True, color=[255,0,0], thickness=2)    

plt.figure()
plt.imshow(img_dst)
plt.show()

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
  
# Warp source image to destination based on homography
img_out = cv2.warpPerspective(img_src, h, (img_dst.shape[1], img_dst.shape[0]))
cv2.imshow("Warped", img_out)
cv2.waitKey(0)

cv2.imwrite("output/beachVolleyball.jpg", img_out)		