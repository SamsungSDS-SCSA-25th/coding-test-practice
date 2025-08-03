# 7 X 6 행렬에서 김밥던지기
# 김밥을 던지면 가장 아래로 내려감
# 그 이후 4개가 가로세로대각선 기준으로 연속하는지 확인
# 아래에서 matrix 전체 완전탐색 -> (1,0),(0,1),(1,1),(1,-1) 4방향

directions = [(1,0),(0,1),(1,1),(1,-1)]

matrix = [ [0]*7 for _ in range(6) ]

# 상근이 김밥: 1 / 정인이 김밥: 2
flag = False
if not flag:
    for ansIdx in range(21):
        sCol, jCol = map(int, input().split())
        sCol -= 1 # 열의 번호는 1번부터 시작함
        jCol -= 1

        # 쌓기
        for row in range(6):
            if matrix[row][sCol] == 0:
                matrix[row][sCol] = 1
                break
        # 확인
        for row in range(6):
            for col in range(7):
                if matrix[row][col] == 1:
                    for dx, dy in directions:
                        length = 0
                        for dist in range(4):
                            # print(f'{length=}')
                            nxtRow, nxtCol = row + dy*dist, col + dx*dist
                            if 0<=nxtRow<6 and 0<=nxtCol<7 and matrix[nxtRow][nxtCol] == 1:
                                length += 1
                            else:
                                break
                        if length == 4:
                            flag = True
                            answer = 'sk ' + str(ansIdx+1)
                            break

        if flag:
            break

        # 쌓기
        for row in range(6):
            if matrix[row][jCol] == 0:
                matrix[row][jCol] = 2
                break
        # 확인
        for row in range(6):
            for col in range(7):
                if matrix[row][col] == 2:
                    for dx, dy in directions:
                        length = 0
                        for dist in range(4):
                            nxtRow, nxtCol = row + dy*dist, col + dx*dist
                            if 0 <= nxtRow < 6 and 0 <= nxtCol < 7 and matrix[nxtRow][nxtCol] == 2:
                                length += 1
                            else:
                                break
                        if length == 4:
                            flag = True
                            answer = 'ji ' + str(ansIdx+1)
                            break

        if flag:
            break

        # print(matrix)

if flag:
    print(answer)
else:
    print('ss')