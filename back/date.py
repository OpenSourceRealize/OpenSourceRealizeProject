# datetime 모듈을 사용할 수 있도록 포함시키기
from datetime import datetime

"""
Firebase에 저장할 
현재 시간과 오늘 날짜 값을
가져오기 위한 함수들 구현
"""

# 현재 시간 구하는 함수
def timenow():
    now = datetime.now() # 현재 시간 가져오기
    string = str(now.year) + "." + str(now.month) + "." + str(now.day) + "." + str(now.hour) + "." + str(
        now.minute) + "." + str(now.second)

    # 현재 시간 값(string)을 호출한 곳으로 return
    return string

# 오늘 날짜를 구하는 함수
def daytoday():
    day = datetime.now() # 오늘 날짜 가져오기
    string = str(day.year) + "-" + str(day.month) + "-" + str(day.day)

    # 현재 시간 값(string)을 호출한 곳으로 return
    return string

