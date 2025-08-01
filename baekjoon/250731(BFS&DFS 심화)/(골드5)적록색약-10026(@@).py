# XO
## 아이디어
# 방문행렬은 전체색을 포함하여 지나갔는지를 확인하는 용도 -> 벽을 다르게 구분하니 일반인과 색약인 방문행렬 구분
# 영역의 크기는 벽의 색을 보고 판단 / 방문행렬은 다시 출발해서 영역을 구해야하는지 판단하는 척도일 뿐
# 조건정리 잘하기!!!

'''
파이썬에서 리스트(또는 2D 리스트) 같은 뮤터블(mutable) 객체를 함수 인자로 넘기면,
그 함수 안에서 visited[y][x] = True 같은 방식으로 내부를 수정해도 원본 객체가 그대로 바뀝니다.
-> Todo) bfs함수 하나로 리팩토링 해보기!
'''
''' #1
from collections import deque

moveList = [(1,0),(-1,0),(0,1),(0,-1)]

def normalBfs(startCol, startRow, allowedColor):
    global rgbMatrix, normalVisited, n
    q = deque([(startCol, startRow)])
    normalVisited[startRow][startCol] = True

    areaCnt = 1
    while q:
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not normalVisited[nxtRow][nxtCol] and rgbMatrix[nxtRow][nxtCol] in allowedColor:
                q.append((nxtCol, nxtRow))
                normalVisited[nxtRow][nxtCol] = True
                areaCnt += 1
    return areaCnt


def blindBfs(startCol, startRow, allowedColor):
    global rgbMatrix, blindVisited, n
    q = deque([(startCol, startRow)])
    blindVisited[startRow][startCol] = True

    areaCnt = 1
    while q:
        currCol, currRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = currCol + dx, currRow + dy
            if 0 <= nxtCol < n and 0 <= nxtRow < n and not blindVisited[nxtRow][nxtCol] and rgbMatrix[nxtRow][nxtCol] in allowedColor:
                q.append((nxtCol, nxtRow))
                blindVisited[nxtRow][nxtCol] = True
                areaCnt += 1
    return areaCnt


n = int(input())
rgbMatrix = [ list(input()) for _ in range(n) ]

normalVisited = [ [False]*n for _ in range(n) ]
blindVisited = [ [False]*n for _ in range(n) ]

# 일반인
normalCnt = 0
for row in range(n):
    for col in range(n):
        if not normalVisited[row][col]:
            normalBfs(col, row, {rgbMatrix[row][col]}) # 행, 열, 색
            normalCnt += 1 # bfs를 다녀온다는 것은 영역이 하나 존재한다는 것
print(normalCnt, end=' ')

# 색약
blindCnt = 0
for row in range(n):
    for col in range(n):
        if not blindVisited[row][col]:
            if rgbMatrix[row][col] == 'R' or rgbMatrix[row][col] == 'G': # 적녹인 경우
                blindBfs(col, row, {'R', 'G'})
                blindCnt += 1
            elif rgbMatrix[row][col] == 'B':
                blindBfs(col, row, {rgbMatrix[row][col]})
                blindCnt += 1
print(blindCnt)
'''
#2 -> 방문행렬을 나누는 기준: 영역을 또갈지 말지에 대한 척도 / 색상마다 나눌필요가 없음
from collections import deque

moveList = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(startCol, startRow, visited, allowedColor):
    global n, rgbMatrix
    q = deque([(startCol, startRow)])
    visited[startRow][startCol] = True # 참조변수라 전역에서도 visited 바뀜

    areaCnt = 1
    while q:
        # print(f'{q=}')
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not visited[nxtRow][nxtCol] and rgbMatrix[nxtRow][nxtCol] in allowedColor: # (D) 조건 유의
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True
                areaCnt += 1

    return areaCnt # 더이상 탐색 할 수 없을때까지

n = int(input())
rgbMatrix = [ list(input()) for _ in range(n) ]

normalVisited = [ [False]*n for _ in range(n) ]
blindVisited = [ [False]*n for _ in range(n) ]

normalCnt, blindCnt = 0, 0
for row in range(n):
    for col in range(n):
        curColor = rgbMatrix[row][col]
        if not normalVisited[row][col]:
            bfs(col, row, normalVisited, {curColor}) # iterable한 객체는 지역에 들어간 연산도 전역에서 바뀜(참조변수) / curColor를 참고하여 탐색
            normalCnt += 1

        if not blindVisited[row][col]:
            if rgbMatrix[row][col] == 'R' or rgbMatrix[row][col] == 'G':
                bfs(col, row, blindVisited, {'R', 'G'}) # 색약인 경우는 RG 둘다 탐색가능
                blindCnt += 1
            else:
                bfs(col, row, blindVisited, {curColor})
                blindCnt += 1

print(normalCnt, blindCnt)