from datetime import datetime


def timenow():
    now = datetime.now()
    string = str(now.year) + "." + str(now.month) + "." + str(now.day) + "." + str(now.hour) + "." + str(
        now.minute) + "." + str(now.second)
    return string

def daytoday():
    day = datetime.now()
    string = str(day.year) + "-" + str(day.month) + "-" + str(day.day)
    return string

