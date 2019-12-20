import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read source image.
img_src = cv2.imread('images/3DCourtBasketball.jpg')

# Four corners of the 3D court + mid-court circle point in source image
pts_src = np.array([
    [126, 113],     # top left corner
    [67, 378],      # bottom left corner (top)
    [143, 379],     # bottom left corner (bottom)
    [637, 150],     # bottom right corner
    [435, 103]      # top right corner
])

cv2.polylines(img_src, [pts_src], isClosed=True, color=[255,0,0], thickness=2)

plt.imshow(img_src)
plt.title('Original')
plt.show()

# Read destination image.
img_dst = cv2.imread('images/2DCourtBasketball.jpg')

# Four corners of the court + mid-court circle point in destination image 
# Start top-left corner and go anti-clock wise + mid-court circle point
pts_dst = np.array([
    [8, 7],         # top left corner
    [4, 333],       # bottom left corner (top)
    [32, 355],       # bottom left corner (bottom)
    [631, 355],     # bottom right corner
    [631, 7]       # top right corner
])

cv2.polylines(img_dst, [pts_dst], isClosed=True, color=[255,0,0], thickness=2)

plt.imshow(img_dst)
plt.title('Original')
plt.show()

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
  
# Warp source image to destination based on homography
img_src2 = cv2.imread('images/3DCourtBasketball.jpg')
img_out = cv2.warpPerspective(img_src2, h, (img_dst.shape[1], img_dst.shape[0]))
cv2.imshow("Warped", img_out)
cv2.waitKey(0)

cv2.imwrite("output/leftViewResult.jpg", img_out)		