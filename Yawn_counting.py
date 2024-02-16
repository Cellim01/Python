        
                #yawn counting                


import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

mpFacemesh = mp.solutions.face_mesh

FaceMesh = mpFacemesh.FaceMesh(max_num_faces=1)

mpDraw = mp.solutions.drawing_utils

DrawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

mouth_was_closed = False

Esneme_Sayısı = 0

while True:
    
    success, img = video.read()

    color_change = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   
    result = FaceMesh.process(color_change)

    if result.multi_face_landmarks:
        for faceLm in result.multi_face_landmarks:
            
            mpDraw.draw_landmarks(img, faceLm, mpFacemesh.FACEMESH_CONTOURS, DrawSpec)

            mouth_landmarks = faceLm.landmark
            
            upper_lip = ( mouth_landmarks[13].y + mouth_landmarks[14].y ) / 2
            
            lower_lip = mouth_landmarks[17].y

            lip_distance = lower_lip - upper_lip

            if lip_distance > 0.090 :  
                
                if not mouth_was_closed :  
                    
                    Esneme_Sayısı += 1
                
                mouth_was_closed = True
            
            else:
                
                mouth_was_closed = False

    cv2.putText(img, f"Esneme Sayisi: { Esneme_Sayısı }", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2 )

    cv2.imshow("Video2", img)

    if cv2.waitKey(20) & 0xFF == ord("q"): break

cv2.destroyAllWindows()
video.release()
