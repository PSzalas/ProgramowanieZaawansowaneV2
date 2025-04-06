import cv2
import numpy as np

def measure_line_thickness(binary_image):
    edges = cv2.Canny(binary_image, 100, 200)
    thickness = np.sum(edges == 255, axis=0)
    thickness = np.max(thickness)
    return thickness

image = cv2.imread("../ExampleImages/binary.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
initial_thickness = measure_line_thickness(gray)
print(f"Line thickness before delatation: {initial_thickness} pixels")

for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    dilated_thickness = measure_line_thickness(dilated)
    print(f"Line thickness after delatation {i + 1} : {dilated_thickness} pixels")
    cv2.imshow("Dilated {} times".format(i + 1), dilated)

cv2.waitKey(0)