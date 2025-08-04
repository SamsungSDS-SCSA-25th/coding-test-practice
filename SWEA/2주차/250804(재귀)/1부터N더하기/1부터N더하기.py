def sumNum(num, totalSum):
    #1 조건
    if num == 0:
        return print(totalSum)
    #2 재귀 전 액션
    totalSum += num
    #3 재귀
    sumNum(num-1, totalSum)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print(f'#{i}', end=' ')
    sumNum(n, totalSum=0)