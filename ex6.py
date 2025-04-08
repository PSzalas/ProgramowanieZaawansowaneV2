import cv2
import numpy as np

image = cv2.imread("../ExampleImages/grey.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

hist = cv2.normalize(hist, hist, 0, 400, cv2.NORM_MINMAX)

hist_img = np.full((400, 512, 3), 255, dtype=np.uint8)

for x in range(1, 256):
    cv2.line(
        hist_img,
        (2*(x-1), 400 - int(hist[x-1].item())),
        (2*x, 400 - int(hist[x].item())),
        (0, 0, 0), 1
    )

otsu_thresh_val, _ = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.line(hist_img,
         (int(2*otsu_thresh_val), 0),
         (int(2*otsu_thresh_val), 400),
         (0, 0, 255), 2)

cv2.putText(hist_img, f'Otsu: {otsu_thresh_val:.0f}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

cv2.imshow("Histogram with Otsu threshold", hist_img)

_, thresh_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Modified image", thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()