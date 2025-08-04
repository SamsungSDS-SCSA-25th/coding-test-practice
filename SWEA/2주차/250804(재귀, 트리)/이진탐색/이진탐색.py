def inOrder(node):
    global cnt, n
    if node <= n:
        inOrder(node*2)
        tree[node] = cnt # 1부터 시작하고, 왼쪽을 다 채움
        cnt += 1
        inOrder(node*2+1) # 마지막으로 오른쪽 구역


t = int(input())
for i in range(1, t+1):
    n = int(input())
    tree = [0] * (n+1)

    cnt = 1
    inOrder(1)

    print(f'#{i} {tree[1]} {tree[n//2]}')