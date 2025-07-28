# 스택을 이용하는 간단한 문제

t = int(input())

for index in range(t):
    charList = list(input())
    # print(charList)
    stack = []
    for char in charList:
        if char == '(' or char == '{': # 여는 괄호는 조건없이 append
            stack.append(char)

        if char == ')' or char == '}': # 닫는 괄호의 조건들
            if not stack: # (D) 엣지케이스 조건 추가 -> 앞에 여는 괄호가 없는데 닫는 괄호
                stack.append(char)
                break

            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and char == '}':
                stack.pop()
            elif char == ')' and stack[-1] == '{': # (D) 엣지케이스 조건 추가 -> 여는괄호의 모양이 다르면 닫는 괄호 append
                stack.append(char)
            elif char == '}' and stack[-1] == '(': # (D) 위 동
                stack.append(char)

        # print(stack)

    if not stack:
        print(f'#{index+1} 1')
    elif stack:
        print(f'#{index+1} 0')