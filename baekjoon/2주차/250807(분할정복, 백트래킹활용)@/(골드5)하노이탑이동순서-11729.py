#1 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
#2 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
#  단, 이동 횟수는 최소가 되어야 한다. -> 가지치기
# n-1개 만큼 2번에 옮기고 -> 마지막을 3번으로 옮김 -> n-1만큼 3번에 옮기기

# 1 2 3
def hanoiTower(N, start, middle, end):
    if N == 1:
        print(start, end)
        return

    hanoiTower(N-1, start, end, middle) # 1단계: N-1...번 1 -> 2 옮기기
    print(start, end) # 2단계: N번째(가장큰원판) 1 -> 3 이동
    hanoiTower(N-1, middle, start, end) # 3단계: N-1...번 2 -> 3 옮기기


N = int(input())
print(2**N-1)
hanoiTower(N, 1, 2, 3)