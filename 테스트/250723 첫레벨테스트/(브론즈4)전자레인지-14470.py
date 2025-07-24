'''
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
'''

# 중복되는 기능 함수화???
meatTemperature = int(input())
targetTemperature = int(input())
upTemperatureIced = int(input())
unfreezeTemperatureIced = int(input())
upTemperatureAir = int(input())

def minusUp(temperature, sec):
    temperature += 1
    sec += upTemperatureIced
    return temperature, sec

def plusUp(temperature, sec):
    temperature += 1
    sec += upTemperatureAir
    return temperature, sec

def zeroUp(temperature, sec):
    sec += unfreezeTemperatureIced
    sec += upTemperatureAir # WARNING. 해동 이후에 1도로 올라가는 시간도 넣어야 함
    temperature += 1
    return temperature, sec

secCnt = 0
while True: # 0을 기준으로, 영하면 해동시간 고려, 영상이면 해동시간 고려 x, 온도가 0인 것은 없음

    if targetTemperature <= meatTemperature: # 공통 내용은 제일 처음 validate
        #print(meatTemperature, secCnt)
        break

    if meatTemperature > 0:
        meatTemperature, secCnt = plusUp(meatTemperature, secCnt)

    elif meatTemperature < 0:
        meatTemperature, secCnt = minusUp(meatTemperature, secCnt)
        #print(meatTemperature, secCnt)

    elif meatTemperature == 0:
        meatTemperature, secCnt = zeroUp(meatTemperature, secCnt)

print(secCnt)
