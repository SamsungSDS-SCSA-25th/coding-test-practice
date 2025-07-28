# 맨 처음 행에 1인 인덱스 찾아서 저장
# 좌우에 1이 있으면 이동한다 그곳으로 이동
# 1. 내려가면서 좌우 1 체크 (0,1) -> (-1,0) & (1,0)
# 2. 좌 or 우로 이동하면서 '0'이나 '초과범위'인지 체크 (-1,0) or (1,0)
# 3. 0이 등장하면 아래로 내려가는 -> 1번 알고리즘으로 돌아감
# 2가지 등장하면 break후 startIdx 반환

### 위로 올라가면 startIdx를 전부 살펴볼 필요가 없음 -> todo

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