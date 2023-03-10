import numpy as np
import cv2

cap = cv2.VideoCapture(0)
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

ref = cv2.imread('onepiece73.jpg', cv2.COLOR_BGR2GRAY)
h,w,_ = ref.shape
ref = cv2.resize(ref,(int(w*0.7),int(h*0.7)))


kp1, des1 = orb.detectAndCompute(ref, None)

while(True):
    _,target = cap.read()

    kp2, des2 = orb.detectAndCompute(target, None)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    result = cv2.drawMatches(ref, kp1, target, kp2, matches[:20], None, flags=2)

    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
