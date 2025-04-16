import cv2

def nothing(x):
    pass

image = cv2.imread("../ExampleImages/foreground.jpg")  # <- zamień na swoją ścieżkę
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

cv2.namedWindow("Segmentation")
cv2.createTrackbar("blockSize", "Segmentation", 3, 25, nothing)  # Suwak: 3-51 (mnożymy x2+1)
cv2.createTrackbar("C", "Segmentation", 20, 40, nothing)         # Suwak: -20 do 20 (przesuniemy o -20)

while True:
    if cv2.getWindowProperty("Segmentation", cv2.WND_PROP_VISIBLE) < 1:
        break
    bs_raw = cv2.getTrackbarPos("blockSize", "Segmentation")
    C_raw = cv2.getTrackbarPos("C", "Segmentation")

    blockSize = bs_raw * 2 + 1
    if blockSize < 3:
        blockSize = 3

    C = C_raw - 20

    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blockSize,
        C
    )

    cv2.imshow("Segmentation", thresh)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()