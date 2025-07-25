# 1~n까지 연속된 조합을 찾음
# DP로도 구현이 가능하다고 함 -> 시간복잡도 고려한다면

''' O(N^2)
n = int(input())
num_list = [ float(input()) for _ in range(n) ]

maxProduct = num_list[0]
for start in range(n):
    tempProduct = 1
    for end in range(start, n):
        tempProduct *= num_list[end]
        if maxProduct < tempProduct:
            maxProduct = tempProduct

print(f'{maxProduct:.3f}')
'''

# O(N) -> 연속된 부분 수열(subarray)의 곱 중 가장 큰 값
n = int(input())
num_list = [ float(input()) for _ in range(n) ]

maxProduct = 1
for idx in range(n):
    tempProduct = 1
    if tempProduct < 1: # 곱을 계속 이어가다가 곱 < 1.0이 되면, 그 구간은 오히려 결과를 작게 만드므로 버리고 새로 시작하는 방식
        maxProduct = max(maxProduct, tempProduct)
        continue
    else:
        tempProduct *= num_list[idx]
        maxProduct = max(maxProduct, tempProduct)

print(f'{maxProduct:.3f}')
