import numpy as np                                                                                          
import cv2

# camera matrix
mtx = [[647.048823, 0.000000, 326.544754], [0.000000, 645.959963, 234.463113], [0.000000, 0.000000, 1.000000]]

# distortion
dist = [0.026716, -0.114498, 0.001072, -0.004303,0.000000]

mtx = np.array(mtx)
dist = np.array(dist)

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    h,  w = frame.shape[:2]

    #calibration
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    cv2.imshow('original.jpg', frame)
    cv2.imshow('calibrated.jpg', dst)

    k = cv2.waitKey(1)
    if k == 0x1b:
        break

cap.release()
cv2.destroyAllWindows()
