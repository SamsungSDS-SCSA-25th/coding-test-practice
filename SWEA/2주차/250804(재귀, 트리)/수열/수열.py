def sequence(n):
    #1 조건
    if n == 1:
        return 1
    #2 재귀
    return sequence(n//2) + sequence(n-1)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    print(sequence(n))