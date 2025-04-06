import cv2

noisy1 = cv2.imread("../ExampleImages/noisy1.jpg")
noisy1_gray = cv2.cvtColor(noisy1, cv2.COLOR_BGR2GRAY)

kernelSizes = [(2, 2), (3, 3), (5, 5), (7, 7)]

cv2.imshow("Noisy1", noisy1)
for kernelSize in kernelSizes:
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, kernelSize)
    opening = cv2.morphologyEx(noisy1_gray, cv2.MORPH_OPEN, kernel_rect)
    cv2.imshow("Kernel_rect opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    closing = cv2.morphologyEx(noisy1_gray, cv2.MORPH_CLOSE, kernel_rect)
    cv2.imshow(f"Kernel_rect closing ({kernelSize[0]}, {kernelSize[1]})", closing)
    gradient = cv2.morphologyEx(noisy1_gray, cv2.MORPH_GRADIENT, kernel_rect)
    cv2.imshow(f"Kernel_rect gradient ({kernelSize[0]}, {kernelSize[1]})", gradient)
    opening = cv2.morphologyEx(noisy1_gray, cv2.MORPH_OPEN, kernel_ellipse)
    cv2.imshow("Kernel_ellipse opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    closing = cv2.morphologyEx(noisy1_gray, cv2.MORPH_CLOSE, kernel_ellipse)
    cv2.imshow(f"kernel_ellipse closing ({kernelSize[0]}, {kernelSize[1]})", closing)
    gradient = cv2.morphologyEx(noisy1_gray, cv2.MORPH_GRADIENT, kernel_ellipse)
    cv2.imshow(f"kernel_ellipse gradient ({kernelSize[0]}, {kernelSize[1]})", gradient)
    opening = cv2.morphologyEx(noisy1_gray, cv2.MORPH_OPEN, kernel_cross)
    cv2.imshow("kernel_cross opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    closing = cv2.morphologyEx(noisy1_gray, cv2.MORPH_CLOSE, kernel_cross)
    cv2.imshow(f"kernel_cross closing ({kernelSize[0]}, {kernelSize[1]})", closing)
    gradient = cv2.morphologyEx(noisy1_gray, cv2.MORPH_GRADIENT, kernel_cross)
    cv2.imshow(f"kernel_cross gradient ({kernelSize[0]}, {kernelSize[1]})", gradient)

for i in range(0, 3):
    eroded = cv2.erode(noisy1_gray.copy(), None, iterations=i + 1)
    dilated = cv2.dilate(noisy1_gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)    

cv2.waitKey(0)