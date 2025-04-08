import cv2

example = cv2.imread("../ExampleImages/example1.jpg")

kernelSizes = [(3, 3), (9, 9), (15, 15)]
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

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

#Która metoda najlepiej usuwa szum?
    #medianBlur

#Która metoda zachowuje najwięcej szczegółów?
    #biliteralFilter aczkolwiek zależy to od parametrów.
    #Drugi najlepszy GaussianBlur

#Jakie są zalety i wady każdej metody?
    #cv2.blur()
        #Zalety:
        #- Prosty i szybki (najmniej wymagający obliczeniowo)
        #- Działa dobrze przy delikatnym wygładzaniu
        #Wady:
        #- Zamazuje krawędzie — nie rozróżnia ich od szumu
        #- Słabo radzi sobie z szumem impulsowym (np. sól i pieprz)
    #cv2.GaussianBlur()
        #Zalety:
        #- Lepsze efekty wizualne niż blur
        #- Mniej zamazuje krawędzie (dzięki wagom)
        #- Naturalne wygładzanie — przypomina ludzkie widzenie
        #Wady:
        #- Nie radzi sobie dobrze z silnym szumem impulsowym
        #- Trochę wolniejsze niż blur()
    #cv2.medianBlur()
        #Zalety:
        #- Świetne na szum impulsowy (sól i pieprz)
        #- Zachowuje krawędzie lepiej niż blur() i GaussianBlur()
        #Wady:
        #- Wolniejsze niż średnie rozmycia (median sortuje wartości)
        #- Może dawać mniej naturalny efekt przy delikatnym rozmyciu
    #cv2.biliteralFilter()
        #Zalety:
        #- Idealne do wygładzania bez zamazywania konturów
        #- Szum kolorowy jest skutecznie redukowany
        #Wady:
        #- obliczenia są kosztowne (każdy piksel analizuje lokalny obszar z wagami)
        #- Trzeba dobrać d, sigmaColor, sigmaSpace – złe wartości mogą dawać słabe efekty