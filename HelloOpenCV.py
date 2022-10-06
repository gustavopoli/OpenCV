import cv2

img = cv2.imread('./images/lena.png')
#img = cv2.imread('./images/lena.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Lena PIS',img)
cv2.waitKey(0)
cv2.destroyAllWindows()