meatTemperature = int(input())
targetTemperature = int(input())
upTemperatureIced = int(input())
unfreezeTemperatureIced = int(input())
upTemperatureAir = int(input())

secCnt = 0
while True:
    if meatTemperature > 0:
        if targetTemperature <= meatTemperature:
            break
        if meatTemperature < 0:  # 얼어있음
            meatTemperature += 1
            secCnt += upTemperatureIced
        elif meatTemperature > 0:  # 상온
            meatTemperature += 1
            secCnt += upTemperatureAir
        elif meatTemperature == 0:  # 해동시간
            secCnt += unfreezeTemperatureIced
            meatTemperature += 1
    elif meatTemperature < 0:
        while meatTemperature <= targetTemperature:
            if meatTemperature < 0: # 얼어있음
                meatTemperature += 1
                secCnt += upTemperatureIced
            elif meatTemperature > 0: # 상온
                meatTemperature += 1
                secCnt += upTemperatureAir
            elif meatTemperature == 0: # 해동시간
                secCnt += unfreezeTemperatureIced
                meatTemperature += 1
    elif meatTemperature == 0:
        secCnt += unfreezeTemperatureIced
        secCnt += ( upTemperatureAir * (targetTemperature - meatTemperature))
        break

print(secCnt)