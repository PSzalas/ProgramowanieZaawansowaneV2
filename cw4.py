import cv2

def cutt_image(startX :int, startY :int, endX :int, endY :int):
    try:
        if not (0 <= startX < w and 0 <= startY < h
        and 0 <= endX < w and 0 <= endY < h):
            raise Exception("Współrzędne poza zakresem obrazu.")

        roi = image[startX:endX, startY:endY]
        cv2.imshow('Roi', roi)
        cv2.waitKey(0)
    except Exception as ex:
        print(f"Błąd: {ex}")

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

print(f"Maksymalna wartość x: {w-1}\n"
      f"Maksymalna wartość y: {h-1}\n\n")

startX = int(input("Podaj współrzędną startX: "))
endX = int(input("Podaj współrzędną endX: "))
startY = int(input("Podaj współrzędną startY: "))
endY = int(input("Podaj współrzędną endY: "))

cutt_image(startX, startY, endX, endY)