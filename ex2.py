import cv2
import imutils

image = cv2.imread("../ExampleImages/fanta2.png")
template = cv2.imread("../ExampleImages/fanta_logo2.png")
rotated30 = imutils.rotate(image, angle=30)
rotated45 = imutils.rotate(image, angle=45)
cv2.imshow("Template", template)

def detect_logo(rotated_img, label):
    cv2.imshow(f"Image {label}", rotated_img)

    imageGray = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    (startX, startY) = maxLoc

    endX = startX + template.shape[1]
    endY = startY + template.shape[0]
    cv2.rectangle(rotated_img, (startX, startY), (endX, endY), (255, 0, 0), 3)
    cv2.imshow(f"{label} output", rotated_img)

    print(f"{label} left-top corner logo coordinates: {maxLoc}")
    print(f"{label} right-bottom corner logo coordinates: ({endX}, {endY})")
    print(f"{label} matching score (maxVal): {maxVal}")

detect_logo(rotated30, "rotated30")
detect_logo(rotated45, "rotated45")
cv2.waitKey(0)