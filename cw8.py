import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
(h, w) = image.shape[:2]
stepX = 150
stepY = 50

for partY in range(0, h-stepY, stepY):
    for partX in range(0, w-stepX, stepX):
        roi = image[partY:(partY+stepY), partX:(partX+stepX)]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)