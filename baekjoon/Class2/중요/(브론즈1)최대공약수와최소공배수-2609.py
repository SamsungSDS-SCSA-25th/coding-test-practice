def divisor(n):
    dList = []
    for i in range(1, n+1):
        if n % i == 0:
            dList.append(i)
    return dList

def greatestCommonDivisor(a, b):
    dA = divisor(a)
    dB = divisor(b)
    #print(f'{dA=} {dB=}')
    cdList = []
    if len(dA) >= len(dB):
        for d in dB:
            if d in dA:
               cdList.append(d)
    else:
        for d in dA:
            if d in dB:
                cdList.append(d)
    return max(cdList)

def leastCommonMultiplier(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            break
        greater += max(a, b)
    return greater

a, b = map(int, input().split())
print(greatestCommonDivisor(a, b))
print(leastCommonMultiplier(a, b))