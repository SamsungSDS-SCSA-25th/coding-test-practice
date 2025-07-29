# 단방향 그래프
# A -> B 가는 일방통행로 있는지? -> 최대깊이까지 가야하므로 DFS

t = 10

def dfs(currentNode):
    global visited, adjMatrix, flag
    visited[currentNode] = True

    for nxtNode in adjMatrix[currentNode]:
        if not visited[nxtNode]:
            if nxtNode == 99:
                flag = True
                break
            dfs(nxtNode)

for _ in range(t):
   index, n = map(int, input().split())
   numList = list(map(int, input().split()))
   adjMatrix = [ [] for _ in range(100) ] # 0~99 고정
   for idx in range(0, len(numList), 2):
       start = numList[idx]
       end = numList[idx+1] # 0~99
       adjMatrix[start].append(end)

   visited = [ False for _ in range(100) ]
   flag = False
   dfs(0)

   if flag:
       print(f'#{index} {1}')
   else:
       print(f'#{index} {0}')