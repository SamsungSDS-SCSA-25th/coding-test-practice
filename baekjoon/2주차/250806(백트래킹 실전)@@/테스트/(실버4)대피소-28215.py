# 대피소가 가능한 조합 -> 백트래킹
# visited 필요 없음 -> 맨해튼 거리만 사용
# 대피소를 설치하는 모든 방법 중 가장 가까운 대피소와 집 사이의 거리 중 가장 큰 값이 가장 작을 때의 거리를 구해라.

def dfs(curDepth, startIdx, placeList):
    global n, k, places, answer
    # 종료조건
    if curDepth == k:
        shelterSet = set(placeList)  # 대피소 인덱스 집합
        maxMinDist = 0

        # 각 집 i에 대해 가장 가까운 대피소까지의 거리 계산
        for i in range(n):
            if i in shelterSet:
                continue
            x1, y1 = places[i]

            # 집 i에서 가장 가까운 대피소 거리
            minDist = float('inf')
            for s in shelterSet:
                x2, y2 = places[s]
                d = abs(x1 - x2) + abs(y1 - y2)
                if d < minDist:
                    minDist = d

            # 최댓값 갱신 및 Pruning
            if minDist > maxMinDist:
                maxMinDist = minDist
                if maxMinDist >= answer: # answer보다 (가까운 대피소와의 거리 최댓값)이 작으면
                    return

        # 글로벌 최적값 갱신
        if maxMinDist < answer:
            answer = maxMinDist
        return

    # 조합 생성
    for i in range(startIdx, n):
        dfs(curDepth + 1, i + 1, placeList + [i])


# 입력 및 초기화
n, k = map(int, input().split())
places = [tuple(map(int, input().split())) for _ in range(n)]

answer = float('inf')
dfs(0, 0, [])
print(answer)