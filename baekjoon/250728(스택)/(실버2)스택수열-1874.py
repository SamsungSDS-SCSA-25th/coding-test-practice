# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# stack에서 pop하는 것 나열한 것이 입력값

n = int(input())
numList = [ int(input()) for _ in range(n) ]
# print(numList)

originList = [ i for i in range(1,n+1) ]
# print(originList)


answerList = []
while True: # stack을 다 쓸 때까지 반복
    numIdx = 0
    for origin in originList:

        if origin != numList[numIdx]: # 값이 다르면 append
            stack.append(origin)
            answerList.append('+')
        elif origin == numList[numIdx]:
            stack.pop()
            answerList.append('+')
            answerList.append('-')

        print(f'{stack=}')
        print(f'{answerList=}')