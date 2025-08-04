def sumNum(num):
    #1 조건
    if num == 0:
        return 0
    #2 재귀
    return sumNum(num-1) + num


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    print(sumNum(n))