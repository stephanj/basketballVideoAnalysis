#
# Author Stephan Janssen
#
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('images/3DBasketballMiddleView.jpg')

plt.imshow(img_src)
plt.title('Original')
plt.show()

# Four corners of the 3D court + mid-court circle point in source image
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_src = np.array([
    [400, 307],     # middle court bottom line
    [400, 218],     # middle circle bottom point
    [644, 217],     # right court corder free throw line bottom corner 
    [570, 189],     # right court corder free throw line top corner
    [160, 204],     # left court corder free throw line bottom corner
    [236, 179],     # left court corder free throw line bottom corner
    ])   

# Read destination image.
img_dst = cv2.imread('images/2DCourtBasketball.jpg')
# cv2.imshow("2D", img_dst)
# cv2.waitKey(0)
plt.figure()
plt.imshow(img_dst)
plt.show()

# Four corners of the court + mid-court circle point in destination image 
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_dst = np.array([
    [317, 351],     # middle court bottom line
    [317, 221],     # middle circle bottom point
    [504, 222],     # right court corder free throw line right corner 
    [504, 137],     # right court corder free throw line left corner
    [132, 222],     # left court corder free throw line bottom corner
    [132, 137]      # left court corder free throw line bottom corner
    ])   

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
  
# Warp source image to destination based on homography
img_out = cv2.warpPerspective(img_src, h, (img_dst.shape[1], img_dst.shape[0]))
cv2.imshow("Warped", img_out)
cv2.waitKey(0)

cv2.imwrite("output/middleViewResult.jpg", img_out)		