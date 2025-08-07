# 양방향 그래프 -> 인접행렬 만들기
# 직접 인접하고 있어야 한다. 2칸 더 가서 인접하면 친구아님
# A-B-C-D-E (깊이가 4까지 갈 수 있는지 체크) -> 백트래킹 (시작하는 사람을 순서대로)

def backTracking(curDepth, curNode):
    global answer
    # 가지치기 -> 이미 존재함을 확인
    if answer:
        return

    # 종료조건
    if curDepth == 4:
        answer = 1
        return

    for nxtNode in adjMatrix[curNode]: # (D) curDepth와 curNode 구분하여 인수로 백트래킹
        if not visited[nxtNode]:
            visited[nxtNode] = True
            backTracking(curDepth + 1, nxtNode)
            visited[nxtNode] = False


N, M = map(int, input().split())
relation = [ tuple(map(int, input().split())) for _ in range(M) ]

adjMatrix = [ [] for _ in range(N) ]
for node1, node2 in relation: # 양방향
    adjMatrix[node1].append(node2)
    adjMatrix[node2].append(node1)

answer = 0
visited = [False] * N

for startNode in range(N): # (D) 각 사람마다 백트래킹하기
    visited[startNode] = True
    backTracking(0, startNode)
    visited[startNode] = False

print(answer)