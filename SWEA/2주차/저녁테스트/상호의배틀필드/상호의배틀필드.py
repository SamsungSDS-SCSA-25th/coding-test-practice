INDEX = list('UDLR')
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def up(c, r, d):
    global matrix, w, h
    matrix[r][c] = '^'
    dx, dy = DIRECTIONS[INDEX.index('U')]
    nc, nr = c + dx, r + dy
    if 0 <= nc < w and 0 <= nr < h and matrix[nr][nc] == '.':
        matrix[r][c] = '.'
        matrix[nr][nc] = '^'
        return nc, nr, 'U'
    return c, r, 'U'  # 회전만 해도 방향은 U로 갱신

def down(c, r, d):
    global matrix, w, h
    matrix[r][c] = 'v'
    dx, dy = DIRECTIONS[INDEX.index('D')]
    nc, nr = c + dx, r + dy
    if 0 <= nc < w and 0 <= nr < h and matrix[nr][nc] == '.':
        matrix[r][c] = '.'
        matrix[nr][nc] = 'v'
        return nc, nr, 'D'
    return c, r, 'D'

def left(c, r, d):
    global matrix, w, h
    matrix[r][c] = '<'
    dx, dy = DIRECTIONS[INDEX.index('L')]
    nc, nr = c + dx, r + dy
    if 0 <= nc < w and 0 <= nr < h and matrix[nr][nc] == '.':
        matrix[r][c] = '.'
        matrix[nr][nc] = '<'
        return nc, nr, 'L'
    return c, r, 'L'

def right(c, r, d):
    global matrix, w, h
    matrix[r][c] = '>'
    dx, dy = DIRECTIONS[INDEX.index('R')]
    nc, nr = c + dx, r + dy
    if 0 <= nc < w and 0 <= nr < h and matrix[nr][nc] == '.':
        matrix[r][c] = '.'
        matrix[nr][nc] = '>'
        return nc, nr, 'R'
    return c, r, 'R'

def shoot(c, r, d):
    global matrix, w, h
    dx, dy = DIRECTIONS[INDEX.index(d)]
    while True:
        c += dx
        r += dy
        if not (0 <= c < w and 0 <= r < h):
            break
        if matrix[r][c] == '*':
            matrix[r][c] = '.'
            break
        if matrix[r][c] == '#':
            break

T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(h)]
    N = int(input())
    moves = input().rstrip()

    # 전차 시작 위치 찾기
    for r in range(h):
        for c in range(w):
            if matrix[r][c] in '^v<>':
                curR, curC = r, c
                dir_map = {'^':'U', 'v':'D', '<':'L', '>':'R'}
                curD = dir_map[matrix[r][c]]
                matrix[r][c] = '.'
                break
        else:
            continue
        break

    # 명령 처리
    for mv in moves:
        if mv == 'U':
            curC, curR, curD = up(curC, curR, curD)
        elif mv == 'D':
            curC, curR, curD = down(curC, curR, curD)
        elif mv == 'L':
            curC, curR, curD = left(curC, curR, curD)
        elif mv == 'R':
            curC, curR, curD = right(curC, curR, curD)
        else:  # 'S'
            shoot(curC, curR, curD)

    # 결과 출력
    symbol = {'U':'^', 'D':'v', 'L':'<', 'R':'>'}
    matrix[curR][curC] = symbol[curD]

    print(f'#{tc} ' + ''.join(matrix[0]))
    for row in matrix[1:]:
        print(''.join(row))
