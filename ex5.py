import cv2

image = cv2.imread("../ExampleImages/trash_can.png")
template = image[50:90, 100:140]
cv2.imwrite("../ExampleImages/trash_can_template.png", template)
cv2.imshow("Template", template)

methods = [
    ("TM_CCOEFF", cv2.TM_CCOEFF),
    ("TM_CCOEFF_NORMED", cv2.TM_CCOEFF_NORMED),
    ("TM_CCORR", cv2.TM_CCORR),
    ("TM_CCORR_NORMED", cv2.TM_CCORR_NORMED),
    ("TM_SQDIFF", cv2.TM_SQDIFF),
    ("TM_SQDIFF_NORMED", cv2.TM_SQDIFF_NORMED)
]

def detect_logo(img, template):
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    for (name, method) in methods:
        result = cv2.matchTemplate(imageGray, templateGray, method)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = minLoc
            match_score = minVal
        else:
            top_left = maxLoc
            match_score = maxVal

        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

        output = img.copy()
        cv2.rectangle(output, top_left, bottom_right, (255, 0, 0), 2)
        cv2.imshow(f"{name} output", output)

        print(f"[{name}] Top-left: {top_left}, Bottom-right: {bottom_right}, Score: {match_score:.4f}")

detect_logo(image, template)
cv2.waitKey(0)
cv2.destroyAllWindows()