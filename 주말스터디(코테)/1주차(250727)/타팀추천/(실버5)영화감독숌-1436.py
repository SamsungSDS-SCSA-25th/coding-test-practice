# 1부터 올리고, 윈도우로 666+이 발견되면 카운트 +1 -> 카운트는 10,000까지

n = int(input())

cnt = 0
num = 665 # (D) N이 1이면 666이 나와야함
while cnt <= 10000:
    num += 1
    for idx in range(len(str(num))-2):
        tempList = []
        for tempIdx in range(idx, idx+3):
            if list(str(num))[tempIdx] == '6': # (D) 문자열...
                tempList.append(6)
        # print(f'{tempList=}')
        if tempList == [6, 6, 6]:
            cnt += 1
            break
    # print(f'{num=}')
    if cnt == n:
        answer = num
        break

print(num)