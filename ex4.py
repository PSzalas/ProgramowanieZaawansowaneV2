import cv2

example = cv2.imread("../ExampleImages/closing.jpg")
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

kernelSizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

cv2.imshow("Original", example)

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(example, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)

for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(example, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)

for k in(3, 9, 15):
    blurred = cv2.medianBlur(example, k)
    cv2.imshow("Median {}".format(k), blurred)

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(example, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)

cv2.waitKey(0)

#Które metody najmocniej rozmywają tekst?
    #Najmocniej Median oraz Average

#Które pozwalają zachować jego czytelność?
    #Zdecydowanie rozmycie dwustronne aczkolwiek Gaussian
    #również niepowoduje nieczytelnego rozmycia