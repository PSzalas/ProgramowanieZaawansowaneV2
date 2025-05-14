import cv2
import imutils
import numpy as np

image = cv2.imread("../ExampleImages/grey.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    x,y,w,h = cv2.boundingRect(c)

    roi = image[y:y+h, x:x+w]
    filename = f'../ExampleImages/kostki/kostka_{i}.png'
    cv2.imwrite(filename, roi)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    cx = x + w // 2
    cy = y + h // 2

    text_pos = (cx - 10, cy - h // 2 - 10)

    segmented_crick = cv2.bitwise_and(image, image, mask=mask)
    cv2.putText(image, f"{i}", text_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255))

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

cv2.imshow("paving_stones", image)

cv2.waitKey(0)
cv2.destroyAllWindows()