def factorial(n):
    #1 조건
    if n == 0:
        return 1
    #2 재귀 + 재귀 후 액션
    return n * factorial(n-1)

t= int(input())
for i in range(1,t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    print(factorial(n))