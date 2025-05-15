import cv2

image = cv2.imread("../ExampleImages/lego.png")
template = cv2.imread("../ExampleImages/lego_template.png")
cv2.imshow("Template", template)

methods = [
    ("TM_CCOEFF_NORMED", cv2.TM_CCOEFF_NORMED),
    ("TM_SQDIFF_NORMED", cv2.TM_SQDIFF_NORMED)
]

def detect_multiple(img, template, method_name, method, threshold=0.8):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template_gray, method)

    if method == cv2.TM_SQDIFF_NORMED:
        loc = zip(*((result <= threshold).nonzero()))
    else:
        loc = zip(*((result >= threshold).nonzero()))

    output = img.copy()
    count = 0
    for pt in loc:
        top_left = (pt[1], pt[0])
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        cv2.rectangle(output, top_left, bottom_right, (0, 255, 0), 2)
        count += 1

    print(f"[{method_name}] Detections: {count}")
    cv2.imshow(f"{method_name} detections", output)

for (name, method) in methods:
    detect_multiple(image, template, name, method, threshold=0.1)

cv2.waitKey(0)
cv2.destroyAllWindows()