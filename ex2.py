import cv2

example = cv2.imread("../ExampleImages/example1.jpg")

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

cv2.waitKey(0)

#Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
    #Efekt rozmycia zwiększa się wraz ze wzrostem wartości kernela

#Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty
#istotnych detali?
    #Im mniejszy tym lepszy, kernel (3,3) zachowuje wystarczającą ilość detali