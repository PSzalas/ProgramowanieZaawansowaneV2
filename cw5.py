import cv2
import imutils

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

def set_pixel_black(x :int, y :int):
    try:
        if not (0 <= x < w and 0 <= y < h):
            raise Exception("Współrzędne poza zakresem obrazu.")

        imutilsShifted = imutils.translate(image, x, y)
        cv2.imshow("ImutilsShifted", imutilsShifted)
        cv2.waitKey(0)
    except Exception as ex:
        print(f"Błąd: {ex}")

print(f"Maksymalna wartość x: {w-1}\n"
      f"Maksymalna wartość y: {h-1}\n\n")

x = int(input("Podaj przesunięcie x: "))
y = int(input("Podaj przesunięcie y: "))

set_pixel_black(x, y)