import cv2
#from matplotlib.pyplot import gray
import numpy as np

wajah_cascade = cv2.CascadeClassifier('Cascades\haarcascade_frontalface_default.xml')
mata_cascade = cv2.CascadeClassifier('Cascades\haarcascade_smile.xml')
deteksi = cv2.VideoCapture(0)

id_wajah =input("Masukkan Id Yang Ingin Anda Buat >>> ")
count = 0
while(True):
    ret, img = deteksi.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    wajah = wajah_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in wajah:
        cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
        count +=1
        cv2.imwrite('capture/wajah/User.'+str(id_wajah)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        mata = mata_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in mata:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imwrite('capture/mata/User.'+str(id_wajah)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
    
    cv2.imshow('image',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif count >= 30:
        break

deteksi.release()
cv2.destroyAllWindows()
