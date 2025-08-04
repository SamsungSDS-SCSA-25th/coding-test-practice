def calculateNode(node):
    info = tree[node]
    if type(info) == int: # 노드가 양의 정수 값이면 float
        return float(info)

    op, left, right = info
    a = calculateNode(left)
    b = calculateNode(right)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b

t = 10
for t in range(1, t+1):
    n = int(input())
    tree = [0] * (n + 1)

    for _ in range(n):
        infoList = input().split()
        nodeIdx = int(infoList[0])
        if infoList[1] in '+-*/':
            tree[nodeIdx] = (infoList[1], int(infoList[2]), int(infoList[3]))
        else:
            tree[nodeIdx] = int(infoList[1])

    ans = calculateNode(1)

    print(f'#{t} {int(ans)}')