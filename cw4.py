import cv2

def set_pixel_black(x :int, y :int):
    try:
        if not (0 <= x < w and 0 <= y < h):
            raise Exception("Współrzędne poza zakresem obrazu.")

        image[y, x] = (0,0,0)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
    except Exception as ex:
        print(f"Błąd: {ex}")

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

print(f"Maksymalna wartość x: {w-1}\n"
      f"Maksymalna wartość y: {h-1}\n\n")

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

set_pixel_black(x, y)