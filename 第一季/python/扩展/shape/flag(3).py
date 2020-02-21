import numpy as np
import cv2

# 创建蓝色背景
img = np.ones((300,500,3),np.uint8)

img[:, :, 0] = 127
img[:, :, 1] = 43
img[:, :, 2] = 0

# 画白色X
img = cv2.line(img,(0,0),(500,300),(255,255,255),50)
img = cv2.line(img,(500,0),(0,300),(255,255,255),50)

#画红色X
img = cv2.line(img,(0,0),(500,300),(58,30,196),30)
img = cv2.line(img,(500,0),(0,300),(58,30,196),30)

#画白色十字
img = cv2.line(img,(0,150),(500,150),(255,255,255),70)
img = cv2.line(img,(250,0),(250,300),(255,255,255),70)

#画红色十字
img = cv2.line(img,(0,150),(500,150),(58,30,196),45)
img = cv2.line(img,(250,0),(250,300),(58,30,196),45)

#显示图片
cv2.imshow('img', img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
