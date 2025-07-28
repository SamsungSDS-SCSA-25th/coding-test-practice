# 스택을 이용한 전형적인 문제
## int로 읽지 않도록 유의

for index in range(10): # 나중에 10으로 바꿔야함
    length, numList = input().split() # (D) int로 읽으면 안됨 -> 맨 앞에 0이면 달라짐
    numList = list(numList)
    # print(numList)

    ### 비밀번호의 길이는 문자열의 길이보다 작다.
    passwordStack = []
    for num in numList:
        if passwordStack: # (D) 스택 구조 템플릿 암기
            if num == passwordStack[-1]:
                passwordStack.pop()
            else:
                passwordStack.append(num)
        else:
            passwordStack.append(num)
        # print(f'{passwordStack=}')

    passwordStr = ''.join(passwordStack)
    print(f'#{index+1} {passwordStr}')