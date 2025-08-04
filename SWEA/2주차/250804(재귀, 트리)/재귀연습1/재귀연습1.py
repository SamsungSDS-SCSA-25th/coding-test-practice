def printNum(num):
    #1 조건
    if num == 0:
        return
    #2 재귀
    printNum(num-1)
    #3 재귀 후 액션
    print(num, end=' ')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i} ', end='')
    printNum(n)
    print()