# (D) 예제3) 꽃을 피우면 더이상 앞으로 진행할 수 없음

from itertools import combinations
from collections import deque

#1  (D) bfs 한번에 들어가고, // (현위치, 색깔, 거리) -> q에 넣고 돌리기
def bfs(startRedList, startGreenList):
    global redInfo, greenInfo
    # 초기화
    q = deque([])
    stateV = [[''] * M for _ in range(N)] # 상태 저장: ''(미방문), 'R', 'G', 'F'
    timeV = [[-1] * M for _ in range(N)] # 시간 저장: -1(미방문) or 도달 시간

    # 초기선언
    # 빨강
    for col, row in startRedList:
        q.append((col, row, 'R', 0))
        stateV[row][col] = 'R'
        timeV[row][col] = 0
    # 초록
    for col, row in startGreenList:
        q.append((col, row, 'G', 0))
        stateV[row][col] = 'G'
        timeV[row][col] = 0

    # 시작
    curFlowers = 0
    while q:
        curCol, curRow, curState, curDist = q.popleft() # 한 칸에 대해서
        # print(f'{curCol=} {curRow=} {curState=} {curDist=}')
        # 현재 칸이 F면 pass
        if stateV[curRow][curCol] == 'F':
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4방향으로
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            # 기본조건 못지키면 pass
            if not (0<=nxtCol<M and 0<=nxtRow<N and matrix[nxtRow][nxtCol] != 0):
                continue

            # 아직 방문한 적이 없다면 gogo
            if stateV[nxtRow][nxtCol] == '' and timeV[nxtRow][nxtCol] == -1:
                q.append((nxtCol, nxtRow, curState, nxtDist))
                stateV[nxtRow][nxtCol] = curState
                timeV[nxtRow][nxtCol] = nxtDist

            ### 위가 아니라, 같은 시간에 도달하여 꽃이 피는 경우
            elif stateV[nxtRow][nxtCol] != curState and timeV[nxtRow][nxtCol] == nxtDist:
                if stateV[nxtRow][nxtCol] != 'F' and stateV[nxtRow][nxtCol] != '':
                    curFlowers += 1
                    stateV[nxtRow][nxtCol] = 'F'

    return curFlowers


N, M, G, R = map(int, input().split())
# 0: 호수 / 1: 배양액불가 / 2: 배양액가능
matrix = [ list(map(int, input().split())) for _ in range(N) ]

#1 배양액 가능한 땅 좌표에서 R+G 만큼 조합 -> 그 안에서 G만큼 조합 (나머지는 R)
possibleList = []
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 2:
            possibleList.append((col, row))

maxFlowers = 0
for comb1 in combinations(possibleList, R+G):
    for comb2 in combinations(comb1, R):
        redList = list(comb2)
        greenList = []
        for temp in list(comb1):
            if temp not in redList:
                greenList.append(temp)
        # ok
        # print(f'{redList=}')
        # print(f'{greenList=}')

        # (D) BFS안에서 배양액 두개를 동시에 굴리면서, F부터는 더이상 진행하지 않으려면 q 안의 값 어떻게 설계?
        curFlowers = bfs(redList, greenList)

        #3 좌표와 거리가 같은 것만 교집합으로 골라낸다 -> 불가
        # curCnt = len( set(redInfo) & set(greenInfo) )
        # 최대개수 업데이트
        maxFlowers = max(maxFlowers, curFlowers)

print(maxFlowers)