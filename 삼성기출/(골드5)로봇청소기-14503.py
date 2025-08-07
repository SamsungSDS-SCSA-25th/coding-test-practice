## validate
# 0은 청소되지 않은 칸 -> 청소하면 2로 처리할 예정
# 1은 벽 -> matrix에서 1인 칸 못가도록 처리
# BFS 아님 그냥 시뮬레이션...

def clean(startCol, startRow, startDir):
    global answer
    # 처음 청소 시작
    matrix[startRow][startCol] = 2
    answer += 1

    endFlag = False
    idx = 0
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)] # (D) 북동남서 -> 좌표때문에 디버깅 했다.. 문제를 잘읽자
    while True:

        if endFlag:
            break

        if not idx:
            curCol, curRow, curDir = startCol, startRow, startDir
        elif idx:
            curCol, curRow, curDir = nxtCol, nxtRow, nxtDir

        # 반시계 방향으로 4칸 확인 후 청소하러 들어감
        for dirIdx in range(1, 5):
            nxtDir = (curDir - dirIdx) % 4
            dx, dy = DIRECTIONS[nxtDir]
            nxtCol, nxtRow = curCol + dx, curRow + dy
            # 반시계 방향으로 돌다가 청소하지 않은 곳으로 전진
            if matrix[nxtRow][nxtCol] == 0: # 1로 둘러쌓여 있어 범위는 안봐도 됨
                matrix[nxtRow][nxtCol] = 2
                answer += 1
                break

        ## 위 4방향 확인 후 -> 청소진행가능한 곳이 없었음 (for-else문)
        # curDir에서 2 더하고 % 4 방향으로 후진 반복
        else:
            backDir = (curDir + 2) % 4
            nxtCol, nxtRow = curCol + DIRECTIONS[backDir][0], curRow + DIRECTIONS[backDir][1]

            # 후진 하는 방향이 벽이면 그대로 멈춘다.
            if matrix[nxtRow][nxtCol] == 1:
                endFlag = True
                break

        idx += 1


# 0 북 / 1 동 / 2 남 / 3 서
N, M = map(int, input().split())
startRow, startCol, startDir = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

answer = 0
clean(startCol, startRow, startDir)
# print(matrix)
print(answer)