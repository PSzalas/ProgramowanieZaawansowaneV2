import cv2

image = cv2.imread('../ExampleImages/example1.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

screen_width = 700
screen_height = 500
cv2.resizeWindow('image', screen_width, screen_height)

cv2.imshow('image', image)

while cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) >= 1:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        cv2.destroyWindow('image')
    elif key == ord('q'):
        break

cv2.destroyAllWindows()