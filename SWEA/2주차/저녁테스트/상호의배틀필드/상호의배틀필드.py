## 모든 조건을 빠짐없이 구현하는 것이 목표!!!

INDEX = list('UDLR')
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def up(curCol, curRow, curDir):
    global matrix, w, h
    matrix[curRow][curCol] = '^' # 회전만 할수도 있으니 전차 방향전환 표시
    dx, dy = DIRECTIONS[INDEX.index('U')]
    nxtCol, nxtRow = curCol + dx, curRow + dy
    if 0 <= nxtCol < w and 0 <= nxtRow < h and matrix[nxtRow][nxtCol] == '.':
        matrix[curRow][curCol] = '.' # 전차가 지나간 자리는 평야
        matrix[nxtRow][nxtCol] = '^' # 전차가 이동한 곳 전차 표시
        return nxtCol, nxtRow, 'U'
    return curCol, curRow, 'U'  # 회전만 해도 방향은 U로 갱신

def down(curCol, curRow, curDir):
    global matrix, w, h
    matrix[curRow][curCol] = 'v'
    dx, dy = DIRECTIONS[INDEX.index('D')]
    nxtCol, nxtRow = curCol + dx, curRow + dy
    if 0 <= nxtCol < w and 0 <= nxtRow < h and matrix[nxtRow][nxtCol] == '.':
        matrix[curRow][curCol] = '.'
        matrix[nxtRow][nxtCol] = 'v'
        return nxtCol, nxtRow, 'D'
    return curCol, curRow, 'D'

def left(curCol, curRow, curDir):
    global matrix, w, h
    matrix[curRow][curCol] = '<'
    dx, dy = DIRECTIONS[INDEX.index('L')]
    nxtCol, nxtRow = curCol + dx, curRow + dy
    if 0 <= nxtCol < w and 0 <= nxtRow < h and matrix[nxtRow][nxtCol] == '.':
        matrix[curRow][curCol] = '.'
        matrix[nxtRow][nxtCol] = '<'
        return nxtCol, nxtRow, 'L'
    return curCol, curRow, 'L'

def right(curCol, curRow, curDir):
    global matrix, w, h
    matrix[curRow][curCol] = '>'
    dx, dy = DIRECTIONS[INDEX.index('R')]
    nc, nr = curCol + dx, curRow + dy
    if 0 <= nc < w and 0 <= nr < h and matrix[nr][nc] == '.':
        matrix[curRow][curCol] = '.'
        matrix[nr][nc] = '>'
        return nc, nr, 'R'
    return curCol, curRow, 'R'

def shoot(curCol, curRow, curDir):
    global matrix, w, h
    dx, dy = DIRECTIONS[INDEX.index(curDir)]
    while True:
        curCol += dx
        curRow += dy
        if not (0 <= curCol < w and 0 <= curRow < h): # 범위 밖으로 넘어가면 끝
            break
        if matrix[curRow][curCol] == '*': # 일반 벽이면 충돌후 벽으로 바뀌고 끝
            matrix[curRow][curCol] = '.'
            break
        if matrix[curRow][curCol] == '#': # 강철 벽이면 충돌후 그냥 끝
            break

tc = int(input())
for i in range(1, tc+1):
    h, w = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(h)]
    N = int(input())
    moves = input().rstrip()

    # 전차 시작 위치 찾기
    for row in range(h):
        for col in range(w):
            if matrix[row][col] in '^v<>':
                curCol, curRow = col, row
                dirDict = {'^':'U', 'v':'D', '<':'L', '>':'R'}
                curDir = dirDict[matrix[row][col]]
                break

    # 명령 처리
    for move in moves:
        if move == 'U':
            curCol, curRow, curDir = up(curCol, curRow, curDir)
        elif move == 'D':
            curCol, curRow, curDir = down(curCol, curRow, curDir)
        elif move == 'L':
            curCol, curRow, curDir = left(curCol, curRow, curDir)
        elif move == 'R':
            curCol, curRow, curDir = right(curCol, curRow, curDir)
        else:  # 'S'
            shoot(curCol, curRow, curDir)

    print(f'#{i} ' + ''.join(matrix[0]))
    for row in matrix[1:]:
        print(''.join(row))