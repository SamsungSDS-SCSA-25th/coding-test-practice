def printReverseNum(num):
    #1 조건
    if num == 0:
        return
    #2 재귀 전 액션
    print(num, end=' ')
    #3 재귀
    printReverseNum(num-1)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    printReverseNum(n)
    print()