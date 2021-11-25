import pytesseract
import re
from date import *
from motor_angle import motorcontrol

def Ocr(img, decodedstr, ref, ref1, a, b, c, d):

    """
    pytesseract를 이용하여 지역 코드 인식하기
    pytesseract로 우리가 3개의 지역을 인식하는 데 필요한 글자인
    0, 1, 2, 3, 7, 8, B, C, D 만 인식하도록 설정
    (영어 대문자 O와 숫자 0을 헷갈려 하기 때문에 둘 다 인식해도 넘어가게 함 )

    해당 프로젝트 프로토 타입에 해당하는 지역 코드는
    107 D02 : 사창동, 303 B01 : 오창읍, 108 C01 : 개신동
    위 코드들이 인식이 되면 연동한 firebase realtime database에 관련된 값 저장

    """

    # 영어, 숫자 중 012378BCD만 인식하도록 설정
    # psm이 11일 때, oem이 1일 때 가장 인식률이 좋음
    text = pytesseract.image_to_string(img, config=" -l eng  -c tessedit_char_whitelist=012378BCD --psm 11 --oem 1")

    # 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되어 있는 지 확인하고 합쳐주기
    text = ''.join(char for char in text if char.isalnum())

    # 띄어쓰기, 개행 없애기
    text = re.sub(r'\n', '', text)


    #text에 매치되는 글자들이 있는 지 확인
    matchObj1 = re.findall('107D02', text)
    matchObj2 = re.findall('107DO2', text)

    matchObj3 = re.findall('108C01', text)
    matchObj4 = re.findall('108CO1', text)

    matchObj5 = re.findall('303B01', text)
    matchObj6 = re.findall('303BO1', text)


    #text와 사창동 코드가 일치한다면 실행
    if matchObj1 or matchObj2 :
        print(matchObj1, "is found - 사창동")
        a = a + 1 # 개수 +1
        string_location= "사창동"
        decodedstr, d = put_database(ref, ref1, a, b, c, d, decodedstr,string_location) # 데이터베이스에 넣는 함수 실행
        motorcontrol("matchObj1")

    #text와 개신동 코드가 일치한다면 실행
    elif matchObj3 or matchObj4 :
        print(matchObj3, "is found - 개신동")
        b = b + 1
        string_location= "개신동"
        decodedstr, d = put_database(ref, ref1, a, b, c, d, decodedstr,string_location)
        motorcontrol("matchObj3")

    # text와 오창읍 코드가 일치한다면 실행
    elif matchObj5 or matchObj6:
        print(matchObj5, "is found - 오창읍")
        c = c + 1 # 개수 1개 플러스
        string_location= "오창읍"
        decodedstr, d = put_database(ref, ref1, a, b, c, d, decodedstr,string_location)
        motorcontrol("matchObj5")

    return a, b, c, d, decodedstr # 해당 값들을 호출한 곳으로 return


def put_database(ref, ref1, a,b,c,d, decodedstr,string_location):
    """
    firebase update 하는 함수
    개수를 총 개수에 더하여 바꾸어 저장하고
    순번과 날짜, 시간 운송장번호, 지역 저장

    """

    ref.update({'사창동': a, '개신동': b, '오창읍': c})
    ref1.update({'순번': str(d), '바코드찍은 날짜': timenow(), '운송장번호': decodedstr, '지역': string_location})
    decodedstr = "" # 운송장 번호 초기화
    d = int(d) + 1
    return decodedstr, d



