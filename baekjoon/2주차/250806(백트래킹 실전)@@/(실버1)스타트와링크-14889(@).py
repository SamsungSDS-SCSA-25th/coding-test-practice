# 대각선은 무조건 0이고 팀을 나누는 선
# 능력치의 차이를 최소 -> 가지치기 가능한 백트래킹 -> n가지 중 n//2가지 고르는 "조합"
# 조합 이후에 matrix 비교 후 min값 갱신

from itertools import combinations

def backTracking(curDepth, startIdx, lst):
    global matrix, minGap, N
    # 가지치기 x
    # 종료조건 -> 조합
    if curDepth == N//2: # 조합 그냥 전부다 돌기 -> *2 만큼 시간복잡도 증가
        # print(f'{lst=}')
        lst2 = [ n for n in range(N) if n not in lst ] # 반대편 lst2 구하기
        # print(f'{lst2=}')

        # 스타트 팀
        startScore = 0
        for comb in list(combinations(lst, 2)):
            s1, s2 = comb[0], comb[1]
            startScore += matrix[s1][s2] + matrix[s2][s1]
        # 링크 팀
        linkScore = 0
        for comb in list(combinations(lst2, 2)):
            l1, l2 = comb[0], comb[1]
            linkScore += matrix[l1][l2] + matrix[l2][l1]

        # print(f'{startScore=} {linkScore=}')
        tempGap = abs(startScore - linkScore)
        minGap = min(tempGap, minGap)
        return

    # 하위재귀
    for startIdx in range(startIdx, N): # (D) N//2 -> N
        backTracking(curDepth + 1, startIdx + 1, lst+[startIdx])


N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

minGap = 10**6
backTracking(0, 0, [])
print(minGap)