# col좌표, row좌표, 이동거리
# 4가지 구역의 조사를 시작
# return 위치 유의

def divideConquer(curCol, curRow, curDist):
    global blueCnt, whiteCnt
    # 종료조건 x -> 왜냐하면 마지막에 길이가 1인 경우 색이 모두 같기 때문에 더이상 재귀하지 않음

    color = matrix[curRow][curCol] # 시작 좌표에서의 색
    for row in range(curRow, curRow + curDist):
        for col in range(curCol, curCol + curDist):
            if matrix[row][col] != color: # 하나라도 시작좌표의 색과 맞지 않다면 -> 분할시킴
                divideConquer(curCol, curRow, curDist//2) # 1분면
                divideConquer(curCol+curDist//2, curRow, curDist//2)  # 2분면
                divideConquer(curCol, curRow+curDist//2, curDist//2)  # 3분면
                divideConquer(curCol+curDist//2, curRow+curDist//2, curDist//2) # 4분면
                return # 함수 종료하고 다음으로 밑으로 내려보냄

    # 위의 조건을 다 버텨낸다면, 모두 같은 색인것
    if color == 1:
        blueCnt += 1
    elif color == 0:
        whiteCnt += 1


N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

blueCnt, whiteCnt = 0, 0
divideConquer(0, 0, N)
print(whiteCnt)
print(blueCnt)