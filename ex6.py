import cv2
import numpy as np

image = cv2.imread("../ExampleImages/example1.jpg")
mask = np.zeros(image.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

rect = (100, 50, 600, 450)

cv2.grabCut(image, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

foreground = image * mask2[:, :, np.newaxis]

blurred = cv2.GaussianBlur(image, (35, 35), 0)

background = blurred * (1 - mask2[:, :, np.newaxis])

result = cv2.add(foreground, background)

cv2.imshow('Depth of field', result)
cv2.waitKey(0)
cv2.destroyAllWindows()