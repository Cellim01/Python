import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# YOLOv4 modelinin yüklenmesi
model = cv2.dnn.readNetFromDarknet("C:\\Users\\user\\Desktop\\yolo\\model\\yolov3.cfg", "C:\\Users\\user\\Desktop\\yolo\\model\\yolov3.weights")

# Sınıf etiketi
labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
                "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
                "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
                "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
                "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
                "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
                "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
                "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
                "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
                "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]


colors = [(0, 255, 255), (0, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0)]

input_width = 416

input_height = 416

while True:
    ret, frame = cap.read()
    if ret == False: break
    

    blob = cv2.dnn.blobFromImage(frame, 1/255, (input_width, input_height), swapRB=True, crop=False)

    model.setInput(blob)
    

    output_layers_names = model.getUnconnectedOutLayersNames()
    
    layer_outputs = model.forward(output_layers_names)
    

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            
            class_id = np.argmax(scores)
            
            confidence = scores[class_id]
            

            if confidence > 0.7:

                center_x = int(detection[0] * frame.shape[1])
                
                center_y = int(detection[1] * frame.shape[0]) 
                
                w = int(detection[2] * frame.shape[1])
                
                h = int(detection[3] * frame.shape[0])
                

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                

                color = colors[class_id]
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                
                cv2.putText(frame, labels[class_id], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()