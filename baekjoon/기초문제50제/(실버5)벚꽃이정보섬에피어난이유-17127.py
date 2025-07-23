""" solve1 -> 브루트포스 O(N^4)
n = int(input())
tree_list = list(map(int, input().split()))

def treeProduct(tempTreeList):
    tempProduct = 1
    for tree in tempTreeList:
        tempProduct *= tree
    return tempProduct

maxSum = 0
for t1 in range(0, n-3):
    for t2 in range(t1+1, n-2):
        for t3 in range(t2+1, n-1):
            for t4 in range(t3+1, n):
                tempSum = 0
                tempSum = treeProduct(tree_list[:t1+1]) + treeProduct(tree_list[t1+1:t2+1]) + treeProduct(tree_list[t2+1:t3+1]) + treeProduct(tree_list[t3+1:])
                #print(f'{tempSum=}')
                if maxSum < tempSum:
                    maxSum = tempSum
print(maxSum)
"""
# solve2 -> 누적곱을 활용해 시간복잡도 O(N^3)으로 최적화
n = int(input())
tree_list = list(map(int, input().split()))

# 누적곱 알고리즘
productPrefix = [1] * (n+1)
for idx in range(1, n+1):
    productPrefix[idx] = productPrefix[idx-1] * tree_list[idx-1] # 마지막에 tree_list임

def treeProduct(start, end): # productPrefix는 0은 임의값 -> 1부터 시작하는 인덱스로 생각
    return productPrefix[end+1] // productPrefix[start]

# 가운데 3개의 경계선 구분(nC3 조합) -> O(N^3)
maxSum = 0
for t1 in range(0, n-3):
    for t2 in range(t1+1, n-2):
        for t3 in range(t2+1, n-1):
                tempSum = 0
                tempSum = treeProduct(0, t1) + treeProduct(t1+1, t2) + treeProduct(t2+1, t3) + treeProduct(t3+1, n-1)
                #print(f'{tempSum=}')
                if maxSum < tempSum:
                    maxSum = tempSum
print(maxSum)

# solve3 -> DP 동적계획법을 활용하여 O(N^2)로 줄이기