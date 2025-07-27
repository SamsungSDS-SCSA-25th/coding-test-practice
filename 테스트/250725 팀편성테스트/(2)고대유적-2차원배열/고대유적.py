# 이 문제는 무난하게 잘풀었다
# 전치행렬 구하는 방법 외워두기 -> 리스트맵리스트집별!
## 0에서 1을 센 것 2보다 큰 지
## 맨 마지막 인덱스에서 1이 등장한 경우 예외처리

t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n) ][::-1]
    matrixT = list(map(list, zip(*matrix)))

    maxLength = 0
    # 열
    for colList in matrix:
        tempCnt = 0
        for idx, col in enumerate(colList):
            if col == 0:
                if tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)
                tempCnt = 0

            elif col == 1:
                tempCnt += 1
                if idx == len(colList)-1 and tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)

    #print(f'{maxLength=}')

    # 행
    for rowList in matrixT:
        tempCnt = 0
        for idx, row in enumerate(rowList):
            if row == 0:
                if tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)
                tempCnt = 0

            elif row == 1:
                tempCnt += 1
                if idx == len(rowList) - 1 and tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)

    print(f'#{index+1} {maxLength}')