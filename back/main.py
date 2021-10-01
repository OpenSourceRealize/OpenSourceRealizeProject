import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from barcode import *
from ocr import *
from date import *

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-application-e7c14-default-rtdb.firebaseio.com/'  # firebase연결
})
ref = db.reference(daytoday() + '/총 개수')

if (db.reference(daytoday()).get()):
    print('존제함')
    a = db.reference(daytoday() + '/총 개수/사창동').get()
    b = db.reference(daytoday() + '/총 개수/개신동').get()
    c = db.reference(daytoday() + '/총 개수/오창읍').get()
    d = a + b + c+1
    print(d)
else:
    ref.update({'사창동': 0, '개신동': 0, '오창읍': 0})
    a = 0
    b = 0
    c = 0
    d = 1

cap = cv2.VideoCapture(1)  # camera start
print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
decodedstr = ""
while (True):
    if cv2.waitKey(1) == ord('q'):
        break
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('result', img)
    if decodedstr == "":
        decodedstr = barcode(img, decodedstr)
    else:
        ref1 = db.reference(daytoday() + '/list/'+str(d))
        a, b, c, d, decodedstr = Ocr(img, decodedstr, ref,ref1, a, b, c, d)

cap.release()
cv2.destroyAllWindows()
