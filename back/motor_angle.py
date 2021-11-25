from dynamikontrol import Module
import time

module = Module()

def motorcontrol(match):
    if match == "matchObj1": #사창동
        module.motor.angle(0)
        time.sleep(10)
        module.motor.angle(0)

    elif match == "matchObj3": #개신동
        module.motor.angle(-45)
        time.sleep(10)
        module.motor.angle(0)

    elif match == "matchObj5": #오창읍
        module.motor.angle(45)
        time.sleep(10)
        module.motor.angle(0)