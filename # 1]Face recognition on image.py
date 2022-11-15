import sys
import cv2

#load the cascade
face_cascade=cv2.CascadeClassifier(r'...')
#read the input video
a=cv2.VideoCapture(0)
print(a)
while True:
    b,c=a.read()
    if(b==True and c is not None):
        c=cv2.resize(c,(1000,1000))
        #convert into multiscale
        gray=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
        #detect faces
        faces=face_cascade.detectMultiScale(gray,1.2,8)#(gray factor,scaling vales,neighbour points)

        #DRAW RECTANGLE AROUNG FACES
        for (x,y,w,h) in faces:
            cv2.rectangle(c,(x,y),(x+w,y+h),(225,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(c,"face",(x,y),font,2,(0,0,225))
        
        cv2.imshow('video',c)
        if ord('q')==cv2.waitKey(20):
            cv2.destroyAllWindows()
            break
    else:
        break

cv2.destroyAllWindows()
a.release()