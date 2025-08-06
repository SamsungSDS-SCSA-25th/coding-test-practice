from collections import deque

t = int(input())
for index in range(t):
    numList = list(map(int, input().split()))
    numQ = deque(numList)
    flag = True
    while True:
        for val in range(1, 6): # 한 사이클
            numQ.rotate(-1)
            if numQ[-1] - val <= 0: # break 시점
                numQ[-1] = 0
                flag = False
                break
            else:
                numQ[-1] -= val

        if not flag:
            break

    ansList = list(numQ)
    print(f'#{index+1}', *ansList)