def allSum(n):
    #1 조건
    if n // 10 == 0:
        return n % 10
    # print(f'{n=}')
    #2 재귀
    return allSum(n//10) + (n % 10)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    print(allSum(n))