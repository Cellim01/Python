
                #Face Mesh 


import cv2
import mediapipe as mp

video = cv2.VideoCapture("C:\\Users\\user\\Desktop\\Python OpenCV ile Sıfırdan Uzmanlığa Görüntü İşleme (Gİ-1)\\3_Görüntü İşleme Projeleri\\6_face_mesh\\video1.mp4")

mpFacemesh = mp.solutions.face_mesh

FaceMesh = mpFacemesh.FaceMesh(max_num_faces = 1)

mpDraw = mp.solutions.drawing_utils

DrawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    
    success, img = video.read()

    if not success:
        
        break

    color_change = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = FaceMesh.process(color_change)

    if result.multi_face_landmarks:
        
        for faceLm in result.multi_face_landmarks:
            
            mpDraw.draw_landmarks(img, faceLm, mpFacemesh.FACEMESH_CONTOURS,DrawSpec)
            
            for id, lm in enumerate(faceLm.landmark):
                
                h, w, c = img.shape
                
                c_x, c_y = int(lm.x*w), int(lm.y*h)
                
                print(id, c_x, c_y )
                
    cv2.imshow("Video2", img)

    if cv2.waitKey(20) & 0xFF == ord("q"):break


cv2.destroyAllWindows()
video.release()