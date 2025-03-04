import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
image_grayscale = cv2.imread('../ExampleImages/example1_grayscale.jpg')

cv2.imshow('Image', image)
cv2.imshow('Image_grayscale', image_grayscale)

while cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) >= 1 or cv2.getWindowProperty('Image_grayscale', cv2.WND_PROP_VISIBLE) >= 1:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        cv2.destroyWindow('Image')
    elif key == ord('2'):
        cv2.destroyWindow('Image_grayscale')
    elif key == ord('q'):
        break

cv2.destroyAllWindows()