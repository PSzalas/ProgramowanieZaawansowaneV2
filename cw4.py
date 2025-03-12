import imutils
import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

def rotate_picture(rotation_degree :int):
    try:
        M = cv2.getRotationMatrix2D((cX, cY), rotation_degree, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        cv2.imshow("Original", image)
        cv2.imshow("Rotated", rotated)
        cv2.waitKey(0)
    except Exception as ex:
        print(f"Błąd: {ex}")

rotation_degree = int(input("Podaj kąt obrotu: "))

rotate_picture(rotation_degree)