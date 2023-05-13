import cv2
image = cv2.imread("C:/Users/student/Downloads/download.jfif")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
image_yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
cv2.imshow('image', image_rgb)
cv2.imshow('image', image_hsv)
cv2.imshow('image', image_gray)
cv2.imshow('image', image_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()

