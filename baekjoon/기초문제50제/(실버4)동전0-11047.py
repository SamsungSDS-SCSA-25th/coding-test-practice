n, m = map(int, input().split())
coin_list = [ int(input()) for _ in range(n) ]
coin_list = sorted(coin_list, reverse=True)

coinCnt = 0
for coin in coin_list:
    if m == 0:
        break
    if coin <= m:
        coinCnt += m // coin
        m = m % coin
        #print(m, coinCnt)

print(coinCnt)

