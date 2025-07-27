# 행렬 입력받는 것을 한 번 뒤집어줘야 함...
# 전치행렬 구하는 파이썬 문법 암기하기!!!
## 0이 등장할 때, 앞에 k개가 쌓여 있는지
## 맨 마지막 1로 끝날 때, k개가 쌓여 있는지
### 아이디어를 코드로 구조화하는 연습이 필요함 -> 한번 반복목 문장을 잘못짜면 계속 고생함..


t = int(input())

for index in range(t):
    n, k = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    matrixT = list(map(list, zip(*matrix)))

    #print(matrix)
    #print(matrixT)

    testCnt = 0
    for colList in matrix:
        tempCnt = 0
        for idx in range(n):
            if colList[idx] == 1:
                tempCnt += 1
                if idx == n-1 and tempCnt == k:
                    testCnt += 1

            if colList[idx] == 0:
                if tempCnt == k:
                    testCnt += 1
                    tempCnt = 0
                tempCnt = 0

    #print(f'{testCnt=}')

    for rowList in matrixT:
        tempCnt = 0
        for idx in range(n):
            if rowList[idx] == 1:
                tempCnt += 1
                if idx == n - 1 and tempCnt == k:
                    testCnt += 1

            if rowList[idx] == 0:
                if tempCnt == k:
                    testCnt += 1
                    tempCnt = 0
                tempCnt = 0

    print(f'#{index+1} {testCnt}')