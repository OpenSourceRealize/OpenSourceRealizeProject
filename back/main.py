import cv2
from barcode import *
from ocr import *
import time
from open_firebase import *


firebase_url = 'https://osori-f3f1a-default-rtdb.asia-southeast1.firebasedatabase.app/' # firebase_url에 파이어베이스 URL 넣어주기
ref, db, a, b, c, d = open_firebase(firebase_url) # open_firebase 실행

decodedstr = ""

cap = cv2.VideoCapture(1)  # camera start
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while (True):
    if cv2.waitKey(1) == ord('q'): # 키보드 q 누르면 종료
        break
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('result', img) # 화면 상에 출력시키기

    # dedodedstr이 비어있으면 barcode부터 인식하여 운송장번호가져와서 운송장번호 string으로 넣어주기
    # decodedstr이 빈 값이 아니면 파이어베이스 경로 정해주고 OCR함수 실행시키기

    if decodedstr == "":
        decodedstr = barcode(img, decodedstr)
    else:
        ref1 = db.reference(daytoday() + '/list/'+str(d))
        a, b, c, d, decodedstr = Ocr(img, decodedstr, ref,ref1, a, b, c, d)
        time.sleep(3)



cap.release()
cv2.destroyAllWindows()
