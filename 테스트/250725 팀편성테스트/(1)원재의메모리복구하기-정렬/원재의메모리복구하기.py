# XO
# 처음에 무슨 소리인가 당황...
## 집에 와서 다시 읽어보니 바로 이해되네... -> 너무 빠르게 읽으려고 하지말자
## 아이디어는 직접 써봐야 나온다.

t = int(input())

for index in range(t):
    originMemory = list(map(int, list(input())))
    zeroMemory = [ 0 for _ in range(len(originMemory)) ]
    # 00000 -> originMemory
    # print(originMemory)
    changeCnt = 0
    for idx, digit in enumerate(originMemory):
        if digit == zeroMemory[idx]:
            continue
        elif digit != zeroMemory[idx]:
            changeCnt += 1
            for tempIdx in range(idx, len(originMemory)):
                zeroMemory[tempIdx] = digit

    # print(changeCnt)
    print(f'#{index+1} {changeCnt}')