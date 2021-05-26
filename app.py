import cv2
import numpy as np
from tensorflow.keras.models import load_model
from scipy.spatial import distance

cap = cv2.VideoCapture(1)

face_model = cv2.CascadeClassifier('./haarCascade/haarcascade_frontalface_default.xml')
classify_model = load_model("./model/classify_model.h5")
mask_label = {0:'Has Mask!',1:'No Mask'}

dist_label = {0:(0,255,0),1:(255,0,0)}
MIN_DISTANCE = 0

while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
        faces = face_model.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
                
        if len(faces)>=1:
            label = [0 for i in range(len(faces))]
            for i in range(len(faces)-1):
                for j in range(i+1, len(faces)):
                    dist = distance.euclidean(faces[i][:2],faces[j][:2])
                    if dist<MIN_DISTANCE:
                        label[i] = 1
                        label[j] = 1
            new_img = cv2.cvtColor(gray, cv2.COLOR_RGB2BGR) #colored output image
            for i in range(len(faces)):
                (x,y,w,h) = faces[i]
                crop = new_img[y:y+h,x:x+w]
                crop = cv2.resize(crop,(150,150))       
                crop = np.reshape(crop,[1,150,150,3])/255.0
                mask_result = classify_model.predict(crop)
                cv2.putText(frame,mask_label[round(mask_result[0][0])],(x, y+90), cv2.FONT_HERSHEY_SIMPLEX,0.5,dist_label[label[i]],2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),dist_label[label[i]],2)
            cv2.imshow("video",frame)
                            

        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()
