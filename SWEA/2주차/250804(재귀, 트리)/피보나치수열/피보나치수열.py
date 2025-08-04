def fibonacci(n):
    #1 조건
    if n == 1 or n == 2:
        return 1
    #2 재귀
    return fibonacci(n-1) + fibonacci(n-2)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    print(fibonacci(n))