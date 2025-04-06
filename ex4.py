import cv2

closing = cv2.imread("../ExampleImages/closing.jpg")
closing_gray = cv2.cvtColor(closing, cv2.COLOR_BGR2GRAY)

kernelSizes = [(2, 2), (3, 3), (5, 5), (7, 7)]

cv2.imshow("Closing_gray", closing_gray)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(closing_gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("MORPH_RECT: ({}, {})".format(
    kernelSize[0], kernelSize[1]), closing)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    closing = cv2.morphologyEx(closing_gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("MORPH_ELLIPSE: ({}, {})".format(
    kernelSize[0], kernelSize[1]), closing)


cv2.waitKey(0)