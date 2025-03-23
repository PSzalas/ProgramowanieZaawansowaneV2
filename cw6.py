import imutils
import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(cY, cX) = (h // 2, w // 2)

def flip_image(flip_direction :int):
    try:
        if not [-1, 0, 1].__contains__(flip_direction):
            raise Exception("Incorrect flip direction")

        flipped = cv2.flip(image, flip_direction)
        cv2.imshow("Flipped", flipped)
        cv2.waitKey(0)
    except Exception as ex:
        print(f"Error: {ex}")

print("Available flip directions:\n"
      "  Horizontal: 1"
      "  Vertical: 0"
      "  Both: -1\n")

flip_direction = int(input("Type key assigned to desired flip direction: "))

flip_image(flip_direction)