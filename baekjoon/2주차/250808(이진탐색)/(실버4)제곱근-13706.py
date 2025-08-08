# 제곱근 구하기
# 보통 제곱근은 중앙 이전에 있으므로, 이진탐색이 유리
## (D) numList가 너무 길어서 메모리초과
## -> numList 없이, 그냥 start, end 비교

def binarySearch(N):
    start = 1
    end = N // 2

    while start <= end:
        mid = (start+end)//2

        if mid**2 == N:
            return mid

        elif mid**2 > N:
            end = mid - 1
        else:
            start = mid + 1

    return 0

N = int(input())
answer = binarySearch(N)
print(answer)