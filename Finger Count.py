# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:41:23 2024

@author: user
"""

import cv2 
import mediapipe as mp


cam = cv2.VideoCapture (0)

mpHand = mp.solutions.hands

hands = mpHand.Hands(max_num_hands=1)

mpDraw = mp.solutions.drawing_utils

uc_noktalar = [4,8,12,16,20]

while True:
    
    LmList = []
    
    success, img = cam.read()
    
    color_change = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    result = hands.process(color_change)
    
    print(result.multi_hand_landmarks)
    
    if result.multi_hand_landmarks:
        
        for handLms in result.multi_hand_landmarks:
            
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
        
            for id,lm in enumerate(handLms.landmark):
                
                h, w, c = img.shape
        
                c_x, c_y = int(lm.x*w), int(lm.y*h)   
                
                LmList.append([id,c_x,c_y])
                
                print(LmList)
        
    if len(LmList) != 0:
        
        fingers = []
        
        if LmList[uc_noktalar[0]][1] > LmList[uc_noktalar[0]-1][1]:
            
            fingers.append(1)
            
        else: fingers.append(0)
        
        for id in range(5):
            
            if LmList[uc_noktalar[id]][2] < LmList[uc_noktalar[id]-2][2]:
                      
                fingers.append(1)
            
            else: fingers.append(0) 

        parmak_sayisi = fingers.count(1)
        
        cv2.putText(img, str(int(parmak_sayisi)-1), (10,150), cv2.FONT_HERSHEY_PLAIN,10, (255,0,0))
        
    cv2.imshow("cam_2", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cam.release()

cv2.destroyAllWindows()