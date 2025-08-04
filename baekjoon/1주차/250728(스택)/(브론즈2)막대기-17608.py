# 스택을 활용해서, stack에 원소가 있고 마지막자리가 클때까지 삭제

n = int(input())
numList = [ int(input()) for _ in range(n) ]
stack = []
for num in numList:

    while stack and num >= stack[-1]:
        stack.pop()
    stack.append(num)

print(len(stack))