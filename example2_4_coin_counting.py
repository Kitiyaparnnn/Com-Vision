#Download images from https://drive.google.com/file/d/1KqllafwQiJR-Ronos3N-AHNfnoBb8I7H/view?usp=sharing

#Bonus from this challenge https://docs.google.com/document/d/1q96VgmpJXlC95h9we-jiuxonEoYrZoqgTD2wjGk5TlI/edit?usp=sharing

import cv2
import numpy as np

def coinCounting(filename):
    im = cv2.imread(filename)
    # target_size = (int(im.shape[1]/4),int(im.shape[0]/4))
    size = im.shape[1]
    target_size = (600,480)
    im = cv2.resize(im,target_size)

    #b,g,r
    mask_yellow = cv2.inRange(im, (0, 150, 150), (120, 255, 255))
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV) 
    mask_blue = cv2.inRange(hsv,(92,50,115),(130,255,255)) #92 110 115 - 130 255 255

    mask_yellow = cv2.medianBlur(mask_yellow, 7)
    mask_blue = cv2.medianBlur(mask_blue, 7)


    #opening for yellow
    kernel_y = np.ones((5,18), np.uint8) #want to connect in vertical
    yellow_open = cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel_y)
    kernel_y2 = np.eye(9, dtype=np.uint8)
    yellow_open = cv2.morphologyEx(yellow_open, cv2.MORPH_OPEN, kernel_y2)


    #opening for blue
    kernel_b = np.ones((5,12), np.uint8) 
    blue_open = cv2.erode(mask_blue,kernel_b,iterations=2)
    kernel_b2 = np.ones((3,4), np.uint8)
    blue_open = cv2.erode(blue_open,kernel_b2,iterations=3)
    kernel_b4 = np.ones((2,2), np.uint8)
    blue_open = cv2.dilate(blue_open, kernel_b4, iterations=5)
    if(size >= 1936):
        kernel_b = np.ones((3,12), np.uint8) 
        blue_open = cv2.erode(mask_blue,kernel_b,iterations=3)

    # kernel_b = np.ones((5,12), np.uint8) #want to connect in vertical
    # blue_open = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel_b,iterations=1)
    # kernel_b2 = np.fliplr(np.eye(15, dtype=np.uint8))
    # blue_open = cv2.morphologyEx(blue_open, cv2.MORPH_OPEN, kernel_b2,iterations=1)


    contours_yellow, hierarchy_yellow = cv2.findContours(yellow_open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours_blue, hierarchy_blue = cv2.findContours(blue_open, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    yellow = len(contours_yellow)
    blue = len(contours_blue)

    # print('Yellow = ',yellow)
    # print('Blue = ', blue)

    cv2.imshow('Original Image',im)
    # cv2.imshow('Yellow Coin-No filter', mask_yellow)
    cv2.imshow('Yellow Coin', yellow_open)
    # cv2.imshow('Blue Coin-No filter',mask_blue)
    cv2.imshow('Blue Coin', blue_open)
    cv2.waitKey()

    return [yellow,blue]


for i in range(1,11):
    print(i,":",coinCounting('.\CoinCounting\coin'+str(i)+'.jpg'))
