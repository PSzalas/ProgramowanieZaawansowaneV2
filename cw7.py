import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
(h, w) = image.shape[:2]
(fX, fY) = (w // 3, h // 3)

for partY in range(0, 3, 1):
    for partX in range(0, 3, 1):
        roi = image[(fY*partY):(fY*(partY+1)), (fX*partX):(fX*(partX+1))]
        cv2.imshow(f"Y:{partY} X:{partX}", roi)
        cv2.waitKey(500)

cv2.waitKey(0)