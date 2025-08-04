# 단순히 이중 for문 시간복잡도 유의
# 메모리도 터질 수 있어서 고려해야 함
## 아이디어가 중요함 -> 기하학적인...

t = 4
for _ in range(t):
    x11, y11, x12, y12, x21, y21, x22, y22 = map(int, input().split())

    # 1) 겹침 범위 계산
    xLeft   = max(x11, x21)
    xRight  = min(x12, x22)
    yBottom = max(y11, y21)
    yTop    = min(y12, y22)

    # 2) 겹침 없음
    if xLeft > xRight or yBottom > yTop:
        print('d')
        continue

    # 3) 점 혹은 선 혹은 면
    if xLeft == xRight and yBottom == yTop:
        print('c')   # 한 점
    elif xLeft == xRight or yBottom == yTop:
        print('b')   # 선분
    else:
        print('a')   # 면