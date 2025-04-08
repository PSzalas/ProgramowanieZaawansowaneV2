import cv2

image = cv2.imread("../ExampleImages/car.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
(b, g, r) = cv2.split(image)

for (name, chan) in zip(("B", "G", "R"), (b, g, r)):
    cv2.imshow(name, chan)

for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)