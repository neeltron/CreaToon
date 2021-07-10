import cv2

img = cv2.imread("elon.jpg")
cv2.imwrite('input.jpg', img)

edges = cv2.Canny(img, 100, 200)
cv2.imwrite('canny.jpg', edges)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_1 = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
cv2.imwrite('medianblur.jpg', edges)
