import cv2

noisy1 = cv2.imread("../ExampleImages/noisy1.jpg")
noisy2 = cv2.imread("../ExampleImages/noisy2.png")
noisy1_gray = cv2.cvtColor(noisy1, cv2.COLOR_BGR2GRAY)
noisy2_gray = cv2.cvtColor(noisy2, cv2.COLOR_BGR2GRAY)

kernelSizes = [(2, 2), (3, 3), (5, 5), (7, 7)]

cv2.imshow("Noisy1", noisy1)
cv2.imshow("Noisy2", noisy2)
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(noisy1_gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Noisy1 opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(noisy2_gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Noisy2 opening: ({}, {})".format(
     kernelSize[0], kernelSize[1]), opening)

cv2.waitKey(0)