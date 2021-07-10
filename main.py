import cv2

img = cv2.imread("elon.jpg")
cv2.imwrite('input.jpg', img)

edges = cv2.Canny(img, 100, 200)
cv2.imwrite('canny.jpg', edges)
