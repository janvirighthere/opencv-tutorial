import cv2

img = cv2.imread("assets\dog.jpg", -1)
img = cv2.resize(img, (400, 400))
cv2.imshow("Dog Image", img)
cv2.waitKey(0)
cv2.destoryAllWindows()
