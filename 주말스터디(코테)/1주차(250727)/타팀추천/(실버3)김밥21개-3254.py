# 7 X 6 행렬에서 김밥던지기
# 김밥을 던지면 가장 아래로 내려감
# 그 이후 4개가 가로세로대각선 기준으로 연속하는지 확인
# 아래에서 matrix 전체 완전탐색 -> (1,0),(0,1),(1,1),(1,-1) 4방향

directions = [(1,0),(0,1),(1,1),(1,-1)]

matrix = [ [0]*7 for _ in range(6) ]

def drop(matrix, playerCol, player):
    for row in range(6):
        if matrix[row][playerCol] == 0:
            matrix[row][playerCol] = player
            break

def check4(matrix, player):
    flag = False
    for row in range(6):
        for col in range(7):
            if matrix[row][col] == player:
                for dx, dy in directions:
                    length = 0
                    for dist in range(4):
                        nxtCol, nxtRow = col + dx*dist, row + dy*dist
                        if 0<=nxtCol<7 and 0<=nxtRow<6 and matrix[nxtRow][nxtCol] == player:
                            length += 1
                        else:
                            break

                    if length == 4:
                        flag = True
                        break

    return flag

# 상근이 김밥: 1 / 정인이 김밥: 2
flag = False
if not flag:
    for ansIdx in range(21):
        sCol, jCol = map(int, input().split())
        sCol -= 1 # 열의 번호는 1번부터 시작함
        jCol -= 1

        # 쌓기 -> matrix는 iterable 해서 함수로 들어가도 값 변경됨
        drop(matrix, sCol, 1)

        # 확인
        flag = check4(matrix, 1)

        if flag:
            answer = 'sk ' + str(ansIdx+1)
            break

        drop(matrix, jCol, 2)
        flag = check4(matrix, 2)

        if flag:
            answer = 'ji ' + str(ansIdx + 1)
            break

        # print(matrix)

if flag:
    print(answer)
else:
    print('ss')