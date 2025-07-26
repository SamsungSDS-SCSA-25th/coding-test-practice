# 문제 제대로 읽자.. 하나의 정사각형+1x1도 가능!! -> 여러개의 정사각형이 아님(deque 써야할듯)
# '#'이 들어있는 좌표를 탐색, 저장
# 바운딩박스를 만들어 -> 최소, 최대 좌표 4개 만들어서 그 안에서 #으로 가득차있는지 확인
# x, y -> col, row 로 저장 유의

t = int(input())

for index in range(t):

    n = int(input())
    matrix = [ list(input()) for _ in range(n) ]

    # '#' 좌표 저장 + 최소, 최대 좌표 4개 찾기
    # 최소, 최대 무조건 무한대로 사용하기
    minCol, minRow = float('inf'), float('inf')
    maxCol, maxRow = float('-inf'), float('-inf')
    shapCnt = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == '#': # 바운딩 박스의 최소, 최대 좌표 개념 이해!
                shapCnt += 1 # #개수 카운트
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                minRow = min(minRow, row)
                maxRow = max(maxRow, row)

    #print(f'{minCol=}, {minRow=}, {maxCol=}, {maxRow=}')

    xLength = maxCol - minCol + 1
    yLength = maxRow - minRow + 1
    #print(f'{xLength=}, {yLength=}')

    flag = False
    if shapCnt == xLength*yLength and xLength == yLength: # 정사각형인지 검증
        flag = True

    if flag:
        print(f'#{index + 1} yes')
    elif not flag:
        print(f'#{index + 1} no')