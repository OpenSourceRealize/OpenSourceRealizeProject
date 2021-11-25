import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from date import *

def open_firebase(firebase_url):
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_url  # firebase에 연결하기
    })
    ref = db.reference(daytoday() + '/총 개수')

    if (db.reference(daytoday()).get()):
        print('존재함')
        a = db.reference(daytoday() + '/총 개수/사창동').get()
        b = db.reference(daytoday() + '/총 개수/개신동').get()
        c = db.reference(daytoday() + '/총 개수/오창읍').get()
        d = a + b + c + 1
        print(d)
    else:
        ref.update({'사창동': 0, '개신동': 0, '오창읍': 0})
        a = 0
        b = 0
        c = 0
        d = 1

    return ref, db, a, b, c, d # 해당 값들을 호출한 곳으로 return