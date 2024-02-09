# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:17:46 2024

@author: user
"""


            #HAND TRACKİNG  

import cv2
import mediapipe as mp



cam = cv2.VideoCapture(0)

mpHand = mp.solutions.hands

hands = mpHand.Hands( max_num_hands= 2 )

mpDraw = mp.solutions.drawing_utils



while True:
    
    succes, image = cam.read()
    
    color_change = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    result = hands.process(color_change)
    
    print(result.multi_hand_landmarks)
    
    if result.multi_hand_landmarks :
        
        for handLms in result.multi_hand_landmarks:
            
            mpDraw.draw_landmarks(image, handLms, mpHand.HAND_CONNECTIONS)
    
    cv2.imshow("image", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cam.release()

cv2.destroyAllWindows()
    