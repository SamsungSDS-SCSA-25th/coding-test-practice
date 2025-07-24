n = int(input())

# 약수 구하고 반띵하면됨
# 약수가 짝수 , 홀수

def commonDivisor(n):
    cdList = []
    for i in range(1, n+1):
        if n % i == 0:
            cdList.append(i)
    return cdList

squareCnt = 0
for i in range(1, n+1):
    tempCdList = commonDivisor(i)
    if len(tempCdList) % 2 == 0:
        squareCnt += len(tempCdList) // 2
    elif len(tempCdList) % 2 != 0:
        squareCnt += len(tempCdList) // 2
        squareCnt += 1

print(squareCnt)