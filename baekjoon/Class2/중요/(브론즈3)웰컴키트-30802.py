n = int(input())
numList = list(map(int, input().split()))

primeNumberCnt = 0
for num in numList:
    flag = True
    for idx in range(2, int(num**0.5)+1):
        if num % idx == 0:
            flag = False
            break
    if num == 1:
        flag = False
    if flag:
        primeNumberCnt += 1

print(primeNumberCnt)