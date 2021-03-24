#!/usr/bin/python


from datetime import datetime
import time
from SparkFun_RV8803 import rtc


def main():
    now = datetime.now()
    
    print("RTC Begin: ", rtc.begin())

    rtc.clearAllInterruptFlags()
    rtc.disableAllInterrupts()

    print(rtc.setTimeAll(now.second, now.minute, now.hour, now.weekday(), now.day, now.month, now.year))
    rtc.updateTime()

    print("%s/%s/%s %s:%s:%s" % (
                    rtc.getYear(), 
                    rtc.getMonth(), 
                    rtc.getDate(), 
                    rtc.getHours(), 
                    rtc.getMinutes(), 
                    rtc.getSeconds()
    ))

    rtc.setItemsToMatchForAlarm(True, False, False, False) # Match only to minute hand
    rtc.setAlarmMinutes(42) # Match to 0 minutes each hour
    rtc.enableHardwareInterrupt(3)

    #rtc.setCountdownTimerEnable(True)
    #print(rtc.setCountdownTimerClockTicks(10))
    #print(rtc.getCountdownTimerClockTicks())

    #print(rtc.stringDateUSA())
    #print(rtc.getCountdownTimerEnable())
    #print(rtc.setCountdownTimerEnable(True))
    #time.sleep(1)
    #print(rtc.getCountdownTimerEnable())

    print(rtc.setHundredthsToZero())
    time.sleep(2)

    print(rtc.getInterruptFlag(3))


    rtc.close()


if __name__ == "__main__":
    main()
