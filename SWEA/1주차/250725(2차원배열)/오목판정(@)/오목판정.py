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
            if matrix[row][col] == 'o': # 출발좌표 선택
                for dx, dy in moveList: # 방향 선택
                    tempCol, tempRow = col, row
                    tempCnt = 1
                    while True: # 한 가지 방향에 대해 5개인지 확인
                        if not 0<= tempCol + dx <n or not 0<= tempRow + dy <n:
                            break

                        if matrix[tempRow + dy][tempCol + dx] == 'o':
                            tempCnt += 1
                            tempRow += dy
                            tempCol += dx
                        elif matrix[tempRow + dy][tempCol + dx] == '.':
                            break

                        if tempCnt == 5:
                            flag = True
                            break

    if flag:
        print(f'#{index+1} YES')
    elif not flag:
        print(f'#{index+1} NO')