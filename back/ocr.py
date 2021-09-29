import pytesseract
import cv2
import re
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-application-e7c14-default-rtdb.firebaseio.com/'  # firebase연결
})

ref = db.reference()

a = 1
b = 1
c = 1

cap = cv2.VideoCapture(1)  # camera start
print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while (True):
    if cv2.waitKey(1) == ord('q'):
        break
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img, config=" -l eng  -c tessedit_char_whitelist=012378BCD --psm 11 --oem 1")
    cv2.imshow('result', img)

    text = ''.join(char for char in text if char.isalnum())
    text = re.sub(r'\n', '', text)

    matchObj1 = re.findall('107D02', text)
    matchObj2 = re.findall('107DO2', text)
    matchObj3 = re.findall('108C01', text)
    matchObj4 = re.findall('108CO1', text)
    matchObj5 = re.findall('303B01', text)
    matchObj6 = re.findall('303BO1', text)

    if matchObj1:
        print(matchObj1, "is found - 사창동")
        ref.update({"사창동": a})
        a = a + 1
        time.sleep(10)
    elif matchObj2:
        print(matchObj2, "is found - 사창동")
        ref.update({"사창동": a})
        a = a + 1
        time.sleep(10)
    elif matchObj3:
        print(matchObj3, "is found - 개신동")
        ref.update({'개신동': b})
        b = b + 1
        time.sleep(10)
    elif matchObj4:
        print(matchObj4, "is found - 개신동")
        ref.update({'개신동': b})
        b = b + 1
        time.sleep(10)
    elif matchObj5:
        print(matchObj5, "is found - 오창읍")
        ref.update({'오창읍': c})
        c = c + 1
        time.sleep(10)
    elif matchObj6:

        ref.update({'오창읍': c})
        c = c + 1
        time.sleep(10)
    print(text)

cap.release()
cv2.destroyAllWindows()
