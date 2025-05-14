import cv2
import imutils

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

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

cv2.imshow("300", image)

resized = imutils.resize(image, width=200)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

cv2.imshow("200", image)

resized = imutils.resize(image, width=400)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

cv2.imshow("400", image)

cv2.waitKey(0)
cv2.destroyAllWindows()