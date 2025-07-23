n = int(input())
sizeNumList = list(map(int, input().split()))
t, p = map(int, input().split())

tCnt, pCnt1, pCnt2 = 0, 0, 0
for sizeNum in sizeNumList:
    if sizeNum % t == 0:
        tCnt += sizeNum // t
    else:
        tCnt += sizeNum // t + 1
pCnt1 = n // p
pCnt2 = n % p
print(tCnt)
print(pCnt1, pCnt2)