import numpy as np
import cv2
import matplotlib.pyplot as plt

# 10800 x 21600 resolution, use with caution (memory hungry)
FULL_HEIGHT_MAP_IMAGE_NAME = 'gebco_08_rev_elev_21600x10800.png'
# 294 x 196 resolution
LIGHT_HEIGHT_MAP_IMAGE_NAME = 'srtm_ramp2.worldx294x196.jpg'

img = cv2.imread(LIGHT_HEIGHT_MAP_IMAGE_NAME)

# If you're using FULL_HEIGHT_MAP_IMAGE_NAME as the image file,
# uncomment from "START_RESIZE" till "END_RESIZE" to resize the picture and
# pay attention that even 1 percent on M1 Macbook Air
# is heavy, don't even think about 10 percent!
# START_RESIZE
# scale_percent = 1  # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
# END_RESIZE

img = img[:, :, 0:1]
rows, cols, ch = img.shape


def f(x, y):
    return np.sqrt(img[x, y, 0])


y = range(cols)
x = range(rows)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
