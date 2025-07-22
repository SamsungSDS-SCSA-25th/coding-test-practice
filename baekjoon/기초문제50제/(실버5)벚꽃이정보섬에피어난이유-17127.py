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