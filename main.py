import cv2
import numpy as np
from PIL import Image
image = Image.open("spontaneity.png")
# p = np.array("spontaneity.png")
# print(image.format)
print(image.size)
# print(image.mode)

width, height = image.size
new_size = (width,height)
 
resized_img = image.resize(new_size,resample=Image.Resampling.NEAREST)
def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(image.getpixel((x,y)))
# pixel = image.getpixel((width//2,height//2))
# rgb_only = pixel[:3]
# print(pixel)
# print(rgb_only)
resized_img.save("output_nearest.png")
p = cv2.imread("output_nearest.png")
cv2.namedWindow("image")
cv2.imshow("image",p)
cv2.setMouseCallback("image",mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()

image.close()