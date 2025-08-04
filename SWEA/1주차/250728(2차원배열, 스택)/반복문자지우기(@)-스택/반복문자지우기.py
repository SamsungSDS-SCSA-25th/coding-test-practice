# 스택을 이용하여 연결된 것을 append, pop

t = int(input())

for index in range(t):
    charList = list(input())

    stack = []
    for char in charList:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{index+1} {len(stack)} ')