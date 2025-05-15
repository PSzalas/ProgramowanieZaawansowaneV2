import cv2
import imutils
import numpy as np

image = cv2.imread("../ExampleImages/lego.png")
template = cv2.imread("../ExampleImages/lego_template.png")

resized = imutils.resize(image, width=600)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
MIN_AREA = 200
match_threshold = 0.4

output = image.copy()
rectangles = []
rect_scores = []

for c in cnts:
    area = cv2.contourArea(c)
    if area < MIN_AREA:
        continue

    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    x, y, w, h = cv2.boundingRect(c)

    roi = image[y:y + h, x:x + w]
    if roi.shape[0] < template.shape[0] or roi.shape[1] < template.shape[1]:
        continue

    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(roi_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    match_locations = np.where(result >= match_threshold)
    for (y_off, x_off) in zip(*match_locations):
        rect_x = x + x_off
        rect_y = y + y_off
        rect_w = template.shape[1]
        rect_h = template.shape[0]
        max_val = result[y_off, x_off]

        rectangles.append([rect_x, rect_y, rect_w, rect_h])
        rectangles.append([rect_x, rect_y, rect_w, rect_h])
        rect_scores.append((rect_x, rect_y, rect_w, rect_h, max_val))

grouped_rects, _ = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

def find_best_match_score(grouped, originals, tolerance=3):
    gx, gy, gw, gh = grouped
    best_score = 0.0
    for ox, oy, ow, oh, score in originals:
        if abs(gx - ox) <= tolerance and abs(gy - oy) <= tolerance and abs(gw - ow) <= tolerance and abs(gh - oh) <= tolerance:
            if score > best_score:
                best_score = score
    return best_score

for i, (x, y, w, h) in enumerate(grouped_rects, 1):
    score = find_best_match_score((x, y, w, h), rect_scores)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(f"Match {i}: Score: {score:.3f} Coordinates: Top-left:({x},{y}), Bottom-right:({x + w},{y + h})")

print(f"Number of detections: {len(grouped_rects)}")
cv2.imshow("Detections", output)

cv2.waitKey(0)
cv2.destroyAllWindows()