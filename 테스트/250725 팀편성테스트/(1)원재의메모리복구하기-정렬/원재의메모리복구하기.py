# 처음에 무슨 소리인가 당황...
## 집에 와서 다시 읽어보니 바로 이해되네... -> 너무 빠르게 읽으려고 하지말자
## 아이디어는 직접 써봐야 나온다.

t = int(input())

for index in range(t):
    numList = list(map(int, list(input())))
    emptyList = [0] * len(numList)
    cnt = 0
    for idx, num in enumerate(numList):
        if num == emptyList[idx]:
            continue

        if emptyList[idx] == 0:
            for i in range(idx, len(numList)):
                emptyList[i] = 1
        elif emptyList[idx] == 1:
            for i in range(idx, len(numList)):
                emptyList[i] = 0

        #print(emptyList)

        cnt += 1

    print(f'#{index+1} {cnt}')