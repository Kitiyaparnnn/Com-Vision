import cv2

#Download 'ExampleBGSubtraction.avi' from https://drive.google.com/file/d/1OD_A0wqN2Om2SusCztybu-_hMSUQuRt7/view?usp=sharing

cap = cv2.VideoCapture('ExampleBGSubtraction.avi')

haveFrame,bg = cap.read()

while(cap.isOpened()):
    haveFrame,im = cap.read()

    if (not haveFrame) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

    diffc = cv2.absdiff(im,bg)
    diffg = cv2.cvtColor(diffc,cv2.COLOR_BGR2GRAY)
    bwmask = cv2.inRange(diffg,50,255)

    cv2.imshow('diffc', diffc)
    cv2.moveWindow('diffc',10,10)
    cv2.imshow('diffg',diffg)
    cv2.moveWindow('diffg', 400, 10)
    cv2.imshow('bwmask', bwmask)
    cv2.moveWindow('bwmask', 800, 10)

    cv2.waitKey()

cap.release()
cv2.destroyAllWindows()
