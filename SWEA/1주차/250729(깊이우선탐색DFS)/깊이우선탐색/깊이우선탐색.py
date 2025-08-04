# 여러개의 정점이 연결되어 있을 경우에는 낮은번호의 정점을 우선적으로 방문한다.
# 양방향이다

'''
재귀탬플릿
visited 만들기
정답리스트 만들기
출발노드부터 연결된 이웃노드로 이동
비방문이면, dfs를 하면됨
'''


'''
t = int(input())

# 재귀사용 -> 템플릿 무조건 암기!!!!!!!!!
def dfs(currentNode):

    visited[currentNode] = True
    answerList.append(currentNode)

    for nxt in adjMatrix[currentNode]:
        if not visited[nxt]:
            dfs(nxt)

for index in range(t):
    v,e = map(int,input().split())
    adjMatrix = [[] for _ in range(v+1)] # 그냥 0은 비워두기

    for _ in range(e):
        start, end = map(int,input().split())
        adjMatrix[start].append(end)
        adjMatrix[end].append(start)

    for idx in range(v): # 오름차순 정렬
        adjMatrix[idx].sort()

    # print(adjMatrix)

    answerList = []
    visited = [False] * (v + 1)
    dfs(1)

    print(f'#{index+1}', *answerList)
'''
### 스택으로 DFS 구현

def dfs(curNode):
    global visited, adjMatrix, answerList
    stack = [curNode]
    visited[curNode] = True
    answerList.append(curNode)

    while stack: # 모든 노드를 방문할때까지 -> 원리 나동빈 유튜브 스택원리 참고
        # for-else문
        for nxtNode in adjMatrix[stack[-1]]: # (D) 항상 스택의 마지막을 참고하여 이웃노드 찾기
            if not visited[nxtNode]: # 이웃노드가 존재하여 스택을 추가해야하는 상황
                stack.append(nxtNode)
                visited[nxtNode] = True
                answerList.append(nxtNode)
                break # (D) 일단 이웃노드 찾으면 break
        else: # for문으로 이웃노드 찾았으나 없는 경우
            stack.pop()

t = int(input())
for index in range(t):
    v,e = map(int,input().split())
    adjMatrix = [[] for _ in range(v+1)] # 그냥 0은 비워두기

    for _ in range(e):
        start, end = map(int,input().split())
        adjMatrix[start].append(end)
        adjMatrix[end].append(start)

    for idx in range(v): # 오름차순 정렬
        adjMatrix[idx].sort()

    # print(adjMatrix)

    answerList = []
    visited = [False] * (v + 1)
    dfs(1)

    print(f'#{index+1}', *answerList)