# 완전 이진트리

''' # 루프로 풀기
t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    leafList = [ tuple(map(int, input().split())) for _ in range(m) ]

    tree = [0] * (n+1)
    for leafNode, num in leafList:
        tree[leafNode] = num

    for idx in range(n, 0, -1):
        left, right = 2*idx, 2*idx+1
        if left > n: # 자식노드 존재 X
            continue

        # (D) 오른쪽 자식노드에 대한 처리
        tree[idx] = tree[left] + (tree[right] if right <= n else 0)

    print(f'#{i} {tree[l]}')
'''
# 재귀로 풀기
def postOrder(node):
    if not (1 <= node <= n):
        return 0

    leftSum = postOrder(node*2)
    rightSum = postOrder(node*2 + 1)
    return leftSum + rightSum + tree[node]

t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    leafList = [ tuple(map(int, input().split())) for _ in range(m) ]

    tree = [0] * (n+1)
    for leafNode, num in leafList:
        tree[leafNode] = num

    ans = postOrder(l)
    print(f'#{i} {ans}')