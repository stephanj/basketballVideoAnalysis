import cv2
import numpy as np

# Read source image.
img_src = cv2.imread('images/3DCourtBasketball.jpg')
cv2.imshow("3D", img_src)
cv2.waitKey(0)

# Four corners of the 3D court in source image (start top-left corner and go anti-clock wise)
pts_src = np.array([[125, 128], [70, 350], [622, 163],[391, 112]])

# Read destination image.
img_dst = cv2.imread('images/2DCourtBasketball.jpg')
cv2.imshow("2D", img_src)
cv2.waitKey(0)

# Four corners of the court in destination image (start top-left corner and go anti-clock wise)
pts_dst = np.array([[8, 7],[8, 355],[631, 355],[631, 7]])

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
  
# Warp source image to destination based on homography
img_out = cv2.warpPerspective(img_src, h, (img_dst.shape[1], img_dst.shape[0]))
cv2.imshow("Warped", img_out)
cv2.waitKey(0)