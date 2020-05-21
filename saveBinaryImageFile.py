import cv2 as cv
import sys
img = cv.imread(sys.argv[1])
ima1 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
f=open(sys.argv[2],'wb')
f.write(ima1)
f.close()