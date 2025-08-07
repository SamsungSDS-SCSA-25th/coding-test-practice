# 알파벳이 지금 나온 것과 달라야함 -> 백트래킹
# lst에 쌓아가면 가지치기 하자

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
def backTracking(curCol, curRow, curDepth):
    global visited, maxCnt

    if curDepth > maxCnt:
        maxCnt = curDepth

    if curDepth == 26: # 알파벳 26가지 다 쓰면 조기종료
        return

    for dx, dy in DIRECTIONS:
        nxtCol, nxtRow = curCol + dx, curRow + dy
        if 0<=nxtCol<M and 0<=nxtRow<N and not visited[nxtRow][nxtCol]:
            alphaIdx = ord(matrix[nxtRow][nxtCol]) - ord('A')
            if not alphaVisited[alphaIdx]:
                alphaVisited[alphaIdx] = True
                visited[nxtRow][nxtCol] = True # (D) 방문처리 꼭하기

                backTracking(nxtCol, nxtRow, curDepth + 1)

                alphaVisited[alphaIdx] = False
                visited[nxtRow][nxtCol] = False # 원상복구


N, M = map(int, input().split())
matrix = [ list(input()) for _ in range(N) ]

# 좌표 방문용, 알파벳 방문용 두개로 관리
visited = [ [False]*M for _ in range(N) ]
alphaVisited = [False]*26

startIdx = ord(matrix[0][0]) - ord('A')
visited[0][0] = True
alphaVisited[startIdx] = True

maxCnt = 0
backTracking(0, 0, 1)
print(maxCnt)