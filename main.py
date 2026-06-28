import cv2
import numpy as np
from PIL import Image
image = Image.open("spontaneity.png")

# print(image.format)
print(image.size)
# print(image.mode)

width, height = image.size
new_size = (width,height)

# resized_img = image.resize(new_size,resample=Image.Resampling.NEAREST)
def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        pixel = image.getpixel((x,y))
        print(pixel[:3])
        n = p.copy()
        cv2.putText(n, str(pixel), (650,650), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0),3)
        cv2.imshow("image",n)
# pixel = image.getpixel((width//2,height//2))
# rgb_only = pixel[:3]
# print(pixel)
# print(rgb_only)
p = cv2.imread("spontaneity.png")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",p)
cv2.setMouseCallback("image",mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()

image.close()