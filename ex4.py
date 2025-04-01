import cv2

image = cv2.imread("../ExampleImages/opencv.png")
cv2.imshow("Original", image)

b, g, r = cv2.split(image)

r = cv2.add(r, 50)
image = cv2.merge([b, g, r])

cv2.imshow("Merged", image)

cv2.waitKey(0)
cv2.destroyAllWindows()