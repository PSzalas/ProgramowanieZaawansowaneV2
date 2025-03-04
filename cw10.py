import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

(b, g, r) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print(f"Wynik dla punktu (50,50) r: {r}, g: {g}, b: {b}")
print(f"Wynik dla punktu (200,200) r: {r2}, g: {g2}, b: {b2}\n")
print(f"Różnice r: {max(r, r2)-min(r, r2)}, g: {max(g, g2)-min(g, g2)}, b: {max(b, b2)-min(b, b2)}")
