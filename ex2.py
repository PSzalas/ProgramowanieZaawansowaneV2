import cv2

image = cv2.imread("../ExampleImages/opencv.png")
cv2.imshow("Original", image)

b, g, r = cv2.split(image)

cv2.imshow("Blue channel", b)
cv2.imshow("Green channel", g)
cv2.imshow("Red channel", r)

cv2.waitKey(0)
cv2.destroyAllWindows()