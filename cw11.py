import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

(x, y) = (0, 0)
(b, g, r) = (0,0,0)
for i in range(h):
    for j in range(w):
        (ib, ig, ir) = image[i, j]
        sum_image = sum([int(ib), int(ig), int(ir)])
        sum_current = sum([int(b), int(g), int(r)])
        if sum_image > sum_current:
            (b, g, r) = image[i, j]
            (x, y) = (i, j)

print(f"Wynik dla punktu ({x},{y}) r: {r}, g: {g}, b: {b}")

image[x, y] = (0,0,0)
cv2.imshow('image', image)
cv2.waitKey(0)