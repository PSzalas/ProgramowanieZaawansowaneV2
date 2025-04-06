import cv2

document = cv2.imread("../ExampleImages/medical_scan.png")
document_gray = cv2.cvtColor(document, cv2.COLOR_BGR2GRAY)

kernelSizes = [(2, 10)]

cv2.imshow("Original", document)

dilated = cv2.dilate(document_gray.copy(), None, iterations=1)

for kernelSize in kernelSizes:
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel_ellipse)
    cv2.imshow("Kernel_ellipse opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)

cv2.waitKey(0)