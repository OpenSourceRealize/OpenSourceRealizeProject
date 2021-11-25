# pyzbar 모듈을 사용할 수 있도록 포함시키기
import pyzbar.pyzbar as pyzbar

#바코드 인식 함수
def barcode(img, decodedstr):

    """
    운송장 이미지의 바코드를 인식하여
    운송장번호로 변환시키는 함수
    운송장 번호를 string 반환
    """

    decoded = pyzbar.decode(img)
    if decodedstr == "":
        if decoded != []:
            # 14개의 글자로 이루어진 운송장 번호 일 때 decodedstr에 값 저장
            if len(decoded[0].data.decode('utf-8')) == 14:
                decodedstr = decoded[0].data.decode('utf-8')
                print(decodedstr)
    return decodedstr  # 바코드 값(string)을 호출한 곳으로 return
