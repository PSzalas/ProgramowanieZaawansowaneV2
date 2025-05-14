import cv2
import imutils

image = cv2.imread("../ExampleImages/grey.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(resized_gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

MIN_AREA = 150
MAX_AREA = 5000

widths = []
heights = []
count = 0

for i, c in enumerate(cnts):
    area = cv2.contourArea(c)
    if area < MIN_AREA or area > MAX_AREA:
        continue

    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    x, y, w, h = cv2.boundingRect(c)

    widths.append(w)
    heights.append(h)
    count += 1

    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

if count > 0:
    avg_w = sum(widths) / count
    avg_h = sum(heights) / count
    min_w, max_w = min(widths), max(widths)
    min_h, max_h = min(heights), max(heights)

    print("== Paving stones detection ==")
    print(f"Number of paving stones found: {count}")
    print(f"Average width: {avg_w:.1f} px")
    print(f"Average height: {avg_h:.1f} px")
    print(f"Min size: {min_w}x{min_h} px")
    print(f"Max size: {max_w}x{max_h} px")
else:
    print("Nie wykryto żadnych kostek.")

cv2.imshow("paving_stones", image)
cv2.waitKey(0)
cv2.destroyAllWindows()