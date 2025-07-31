## XX
# 맨 처음 행에 1인 인덱스 찾아서 저장
# 좌우에 1이 있으면 이동한다 그곳으로 이동
# 1. 내려가면서 좌우 1 체크 (0,1) -> (-1,0) & (1,0)
# 2. 좌 or 우로 이동하면서 '0'이나 '초과범위'인지 체크 (-1,0) or (1,0)
# 3. 0이 등장하면 아래로 내려가는 -> 1번 알고리즘으로 돌아감
# 2가지 등장하면 break후 startIdx 반환

### 위로 올라가면 startIdx를 전부 살펴볼 필요가 없음 -> todo

''' #1
t = int(input())

for index in range(t):
    matrix = [ list(map(int, input().split())) for _ in range(100) ]
    startIdxList = [ idx for idx, col in enumerate(matrix[0]) if col == 1 ]
    # print(startIdxList)
    twoFlag, twoAnswer = False, 0
    while not twoFlag:
        for startIdx in startIdxList: # 출발점은 지정하고 시작
            row, col = 0, startIdx
            # transition = [(0, 1), (-1, 0), (1, 0)]
            transitionIdx = 0
            while True:
                # print(f'{transitionIdx=}')
                if matrix[row][col] == 2:
                    twoFlag = True
                    twoAnswer = startIdx
                    break

                if transitionIdx == 0: # 내려가는 방향
                    # print(f'{row=} {col=}')
                    row += 1
                    if row > 99: # (D) 밑으로 내려갔는데 범위 초과면 break
                        break

                    if 0<=col-1<100: # (D) col-1 / col+1 나눔
                        if matrix[row][col-1] == 1:
                            transitionIdx = 1
                    if 0<=col+1<100:
                        if matrix[row][col+1] == 1:
                            transitionIdx = 2

                elif transitionIdx == 1: # 좌로이동
                    # print(f'{row=} {col=}')
                    if 0<=col-1<100:
                        if matrix[row][col-1] == 1:
                            col -= 1
                        elif matrix[row][col-1] == 0: # (D) 0인 경우도 고려해야함
                            transitionIdx = 0
                    else: # 범위 밖이라면
                        transitionIdx = 0

                elif transitionIdx == 2: # 우로이동
                    # print(f'{row=} {col=}')
                    if 0<=col+1<100:
                        if matrix[row][col+1] == 1:
                            col += 1
                        elif matrix[row][col+1] == 0: # (D) 0인 경우도 고려해야함
                            transitionIdx = 0
                    else:  # 범위 밖이라면
                        transitionIdx = 0

            if twoFlag:
                break

    print(f'#{index+1} {twoAnswer}')
'''
#2 -> 아래에서 위로 올라가는 것으로 구하기 (시간복잡도를 줄일 수 있음)

t = int(input())
for index in range(t):
    ladderMatrix = [ list(map(int, input().split())) for _ in range(100) ]
    # 끝점 찾기 -> 2
    endRow = 99
    for col in range(100):
        if ladderMatrix[endRow][col] == 2:
            endCol = col

    nxtCol, nxtRow = endCol, endRow-1
    switchIdx = 0 # 0: up / 1: left / 2: right
    while True:

        if switchIdx == 0: # 위로 올라가는 경우
            upCol, upRow = nxtCol, nxtRow-1
            leftCol, leftRow, rightCol, rightRow = nxtCol-1, nxtRow, nxtCol+1, nxtRow
            if nxtRow == 0: # 시작지점에 도착
                startCol, startRow = nxtCol, 0
                break

            if 0<=leftCol<100 and ladderMatrix[leftRow][leftCol] == 1: # left가 1이면
                nxtCol, nxtRow = leftCol, leftRow
                switchIdx = 1
                continue

            if 0<=rightCol<100 and ladderMatrix[rightRow][rightCol] == 1: # right가 1이면
                nxtCol, nxtRow = rightCol, rightRow
                switchIdx = 2
                continue

            nxtCol, nxtRow = upCol, upRow
            ### 위 조건 중 아무것도 해당하지 않으면, 계속 위로 올라감

        elif switchIdx == 1: # 벽이거나, 0을 leftCol에서 만나는 경우 다시 위로 올라가야함
            leftCol, leftRow = nxtCol-1, nxtRow
            if leftCol<0 or ladderMatrix[leftRow][leftCol] == 0: # 위로 올라가야하는 경우
                nxtCol, nxtRow = nxtCol, nxtRow-1
                switchIdx = 0
                continue

            nxtCol, nxtRow = leftCol, leftRow
            ### 위 조건 중 아무것도 해당하지 않으면, 계속 왼쪽이동

        elif switchIdx == 2: # 벽이거나, 0을 rightCol에서 만나는 경우 다시 위로 올라가야함
            rightCol, rightRow = nxtCol + 1, nxtRow
            if rightCol>99 or ladderMatrix[rightRow][rightCol] == 0:  # 위로 올라가야하는 경우
                nxtCol, nxtRow = nxtCol, nxtRow - 1
                switchIdx = 0
                continue

            nxtCol, nxtRow = rightCol, rightRow
            ### 위 조건 중 아무것도 해당하지 않으면, 계속 왼쪽이동

    print(f'#{index+1} {startCol}')
