import cv2
import numpy as np

img = cv2.imread("variant-4.jpeg")
b, g, r = cv2.split(img)

zeros = np.zeros_like(b)

merge = cv2.merge([b, zeros, zeros])

cv2.imshow("image", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()