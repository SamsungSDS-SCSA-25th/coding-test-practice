# 완전이진트리가 아님
# 재귀란 위에서 아래로 중단시 위로 아래로의 반복과정임을 명심

n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (
        None if left  == '.' else left,
        None if right == '.' else right
    )

# 2) 순회 결과를 담을 리스트
preList = []
inList  = []
postList= []

# 전위 순회 (루트 → 왼쪽 → 오른쪽)
def preOrder(node):
    if node is None:
        return

    preList.append(node) # parent 시작
    preOrder(tree[node][0]) # left로 넘어가서 재귀
    preOrder(tree[node][1]) # right로 넘어가서 재귀

# 중위 순회 (왼쪽 → 루트 → 오른쪽)
def inOrder(node):
    if node is None:
        return

    inOrder(tree[node][0]) # left 최대한 탐색
    inList.append(node) # left 시작 -> 위로 돌아가면 그것이 parent
    inOrder(tree[node][1]) # right 시작

# 후위 순회 (왼쪽 → 오른쪽 → 루트)
def postOrder(node):
    if node is None:
        return

    postOrder(tree[node][0]) # left 최대한 탐색
    postOrder(tree[node][1]) # right 최대한 탐색
    postList.append(node) # 둘 다 다 쓰면 그것이 parent

# 'A'가 root
preOrder('A')
inOrder('A')
postOrder('A')

print(''.join(preList))
print(''.join(inList))
print(''.join(postList))