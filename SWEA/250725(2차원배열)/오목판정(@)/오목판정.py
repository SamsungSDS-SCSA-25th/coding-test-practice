# dxdy 기법으로 찾기

t = int(input())

# 이동방법 리스트 -> 뒤에 있을 것만 보면 됨
# 열이동, 행이동, 대각선 오른쪽, 대각선 왼쪽
moveList = [(1, 0), (0, 1), (1, 1), (-1, 1)]

for index in range(t):
    n = int(input())
    matrix = [ list(input().rstrip()) for _ in range(n) ][::-1]

    flag = False
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'o':
                # 가로
                tempCol, tempCnt = col, 1
                while True:
                    if not 0<=tempCol+moveList[0][0]<n:
                        break
                    if matrix[row][tempCol+moveList[0][0]] == 'o':
                        tempCol += 1
                        tempCnt += 1
                    elif matrix[row][tempCol+moveList[0][0]] == '.':
                        break
                    if tempCnt == 5:
                        flag = True
                        break

                # 세로
                tempRow, tempCnt = row, 1
                while True:
                    if not 0 <= tempRow+moveList[1][1] < n:
                        break

                    if matrix[tempRow+moveList[1][1]][col] == 'o':
                        tempRow += 1
                        tempCnt += 1
                    elif matrix[tempRow+moveList[1][1]][col] == '.':
                        break

                    if tempCnt == 5:
                        flag = True
                        break

                # 대각선 오른쪽
                tempRow, tempCol, tempCnt = row, col, 1
                while True:
                    if not 0 <= tempRow + moveList[2][1] < n or not 0 <= tempCol + moveList[2][0] < n:
                        break

                    if matrix[tempRow + moveList[2][1]][tempCol + moveList[2][0]] == 'o':
                        tempRow += 1
                        tempCol += 1
                        tempCnt += 1
                    elif matrix[tempRow + moveList[2][1]][tempCol + moveList[2][0]] == '.':
                        break

                    if tempCnt == 5:
                        flag = True
                        break

                # 대각선 왼쪽
                tempRow, tempCol, tempCnt = row, col, 1
                while True:
                    if not 0 <= tempRow + moveList[3][1] < n or not 0 <= tempCol + moveList[3][0] < n:
                        break

                    if matrix[tempRow + moveList[3][1]][tempCol + moveList[3][0]] == 'o':
                        tempRow += 1
                        tempCol -= 1
                        tempCnt += 1
                    elif matrix[tempRow + moveList[3][1]][tempCol + moveList[3][0]] == '.':
                        break

                    if tempCnt == 5:
                        flag = True
                        break

    if flag:
        print(f'#{index+1} YES')
    elif not flag:
        print(f'#{index+1} NO')