imageWidth = 512;
imageHeight = 512;
numColor = 3;

import numpy as np
import cv2 as cv
import sys
fd = open(sys.argv[1], 'rb')
f = np.fromfile(fd, dtype=np.uint8,count=imageHeight*imageWidth*numColor)
img = f.reshape((imageHeight, imageWidth, numColor))
ima1 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
fd.close()
cv.imshow('', ima1)
cv.waitKey()
cv.destroyAllWindows()