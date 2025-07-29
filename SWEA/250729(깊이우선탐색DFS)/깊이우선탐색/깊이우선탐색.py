# 여러개의 정점이 연결되어 있을 경우에는 낮은번호의 정점을 우선적으로 방문한다.
# 양방향이다

'''
재귀탬플릿
visited 만들기
정답리스트 만들기
출발노드부터 연결된 이웃노드로 이동
비방문이면, dfs를 하면됨
'''

''' stack 기초
def dfs(start, v):
    # 필요자료형 초기화 및 생성
    visited = [0]*(v+1)
    answerList = []
    stack = []

    # 첫방문시 진행사항
    visited[start] = 1
    answerList.append(start)
    currentNode = start # -> 기준점 설정

    while stack:
        # 연결된, 미방문노드가 있으면 기준점 이동
        for neighbor in adjMatrix[currentNode]:
            if visited[neighbor] == 0:
                stack.append(neighbor) # 되돌아오기 위함
                visited[neighbor] = 1 # 방문처리
                answerList.append(neighbor) # 답에 넣기
                currentNode = neighbor # currentNode 갱신
                break # 새로운 currentNode에서 탐색시작

            else: # break 안함 -> 더이상 갈림길 x
                if stack: # 직접 갈림김
                    currentNode = stack.pop()
                else: # 탐색완료
                    break

    return answerList
'''
'''
def dfs(start):

    # 1
    visited = [0]*(v+1)
    answerList = []
    stack = []

    # 2
    visited[start] = 1
    stack.append(start)
    currentNode = start

    # 3
    while stack:
        for neighbor in adjMatrix[currentNode-1]: # 현재노드에서 연결된 인접노드
            if visited[neighbor] == 0: # 아직 방문안했다면
                visited[neighbor] = 1 # 방문표시
                stack.append(neighbor) # 이웃노드 stack에 추가 -> 깊이를 기록하기 위함
                answerList.append(currentNode)  # 정답에 추가
                currentNode = neighbor
                print(f'{stack=}')
                break # 이웃노드 전체를 순환하지 않는다
        else: # for-else문 -> for문에서 하나도 해당하지 않으면, else문 실행
            if currentNode not in answerList: # (D) 이웃노드 없지만 answerList에 넣어야 하는 경우 (맨끝노드)
                visited[currentNode] = 1
                answerList.append(currentNode)
            stack.pop()
            if not stack: # stack이 공란이면 끝난 것임
                break
            currentNode = stack[-1] # 그 전 노드로

    return answerList
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