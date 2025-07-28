# XO

'''
연속된 N일 이라는 것은 입력값의 길이를 말함... -> 슬라이딩 하며 최고값을 갱신할 필요가 없었던 것
앞에서부터 하면 “현재 위치 이후의 최고가”를 모르기 때문에 매번 뒤를 다시 살펴봐야 하거나 복잡한 자료구조가 필요하지만,
뒤에서부터 한 번 훑으면 정말 단순한 변수 하나로 모든 날의 미래 최고가를 관리할 수 있음
'''

'''
t = int(input())

for index in range(t):
    expectDay = int(input())
    priceList = list(map(int, input().split()))

    maxPrice = float('-inf')
    profit = 0
    for idx, price in enumerate(priceList[::-1]): # 역순으로 max값을 갱신하며 출발 -> 뒤에 max값을 기준으로 사고 판매하기 때문
        if idx == 0: # 맨 뒤에서는 max값 갱신만
            maxPrice = price
            continue
        else: # 그 뒤 idx는 아래 논리
            if price < maxPrice: # 구매 후 판매(가정)
                profit += maxPrice - price
            elif price > maxPrice: # 이후 price에서 maxPrice 갱신
                maxPrice = price

    print(f'#{index+1} {profit}')
'''

# n이 10^6이기 때문에 이중 for문부터 불가
# 모든날을 예측 가능하므로 뒤에서부터 maxPrice 갱신
# 뒤에서부터 idx접근 후 maxPrice보다 작으면 구매-판매 가정

t = int(input())
for index in range(t):
    n = int(input())
    priceList = list(map(int, input().split()))

    maxPrice = float('-inf')
    margin = 0
    for reversePriceIdx, price in enumerate(priceList[::-1]):
        if reversePriceIdx == 0: # 맨 마지막날은 maxPrice만 갱신 -> 구매하지 않으므로
            maxPrice = price
            continue

        if maxPrice > price: # 구매-판매
            margin += maxPrice - price
        elif maxPrice < price: # maxPrice만 갱신, 구매x
            maxPrice = max(price, maxPrice)

    print(f'#{index+1} {margin}')