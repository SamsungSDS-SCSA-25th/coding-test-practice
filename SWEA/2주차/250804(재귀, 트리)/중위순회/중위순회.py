# 완전 이진트리 - 중위순회
# 부모노드 기준 왼쪽자신노드 *2 | 오른쪽자식노드 *2+1

def inOrder(node):
    global n
    if node <= n:
        inOrder(node*2) # 제일 좌측노드로 들어감
        print(tree[node], end='') # 나와서 부모노드로
        inOrder(node*2 + 1) # 오른쪽노드로

t = 10
for i in range(1, t+1):
    n = int(input())
    tree = [''] * (n+1)
    for _ in range(n):
        info = input().split()
        idx = int(info[0])
        tree[idx] = info[1]

    ans =[]
    print(f'#{i}', end=' ')
    inOrder(1)
    print()