import pytesseract
import re
import time
from date import *


def Ocr(img, decodedstr, ref, ref1, a, b, c, d):
    text = pytesseract.image_to_string(img, config=" -l eng  -c tessedit_char_whitelist=012378BCD --psm 11 --oem 1")

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
        print(decodedstr)
        print(timenow())
        a = a + 1
        ref.update( {'사창동': a, '개신동': b, '오창읍': c})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    elif matchObj2:
        print(matchObj2, "is found - 사창동")
        print(decodedstr)
        a = a + 1
        ref.update({'총 개수': {'사창동': a, '개신동': b, '오창읍': c}})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    elif matchObj3:
        print(matchObj3, "is found - 개신동")
        print(decodedstr)
        b = b + 1
        ref.update( {'사창동': a, '개신동': b, '오창읍': c})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    elif matchObj4:
        print(matchObj4, "is found - 개신동")
        print(decodedstr)
        b = b + 1
        ref.update( {'사창동': a, '개신동': b, '오창읍': c})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    elif matchObj5:
        print(matchObj5, "is found - 오창읍")
        print(decodedstr)
        c = c + 1
        ref.update( {'사창동': a, '개신동': b, '오창읍': c})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    elif matchObj6:
        print(matchObj6, "is found - 오창읍")
        print(decodedstr)
        c = c + 1
        ref.update( {'사창동': a, '개신동': b, '오창읍': c})
        ref1.update({'순번' : str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr})
        decodedstr = ""
        d = int(d)+1
        time.sleep(10)
    else:
        print(text)

    return a, b, c, d, decodedstr
