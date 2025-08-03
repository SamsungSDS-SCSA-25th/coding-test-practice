# 방향전환 1, 1, 2, 2, 3, 3 ...
# 북동남서 순으로 계속 순회
# 시작은 n // 2에서 홀수임이 주어짐

n = int(input())
target = int(input())

directions = [(1,0), (1,0), (0,-1), (-1,0)]
matrix = [ [0]*n for _ in range(n) ]
startCol, startRow = n // 2, n // 2
matrix[startRow][startCol] = 1

for num in range(n*n + 1):
    num += 1

    if num == 1:
        curCol, curRow = n // 2, n // 2
        matrix[curRow][curCol] = num

    for dx, dy in directions:
        nxtCol, nxtRow =


    curCol, curRow = nxtCol, nxtRow
