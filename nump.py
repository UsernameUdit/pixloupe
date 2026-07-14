import numpy as np 
import cv2
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([1, 2, 3, 4, 5])
# print(a+b)
# i = np.arange(0,25)

# i = i.reshape((5,5))
# print(i)
# print(i[0:3, 0:2])

# roi = image[startY:endY, startX:endX]
def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        height, width = image.shape[:2]
        r = 25
        top = max(0, y - r)
        bottom = min(height, y + r)
        left = max(0, x - r)
        right = min(width, x + r)
        face = image[top:bottom,left:right]
        resized_relative = cv2.resize(face, None, fx=5.0, fy=5.0, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("face",resized_relative)

image = cv2.imread("ilya.jpg")
cv2.imshow("original",image)
cv2.setMouseCallback("original",mouse_callback)
cv2.waitKey(0)