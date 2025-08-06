# 주어진 확률의 최댓값을 구하라 -> (D) 최대값도 가지치기 하는 방법이 있었음
# 가변적인 요소가 많아서 백트래킹 -> 순열
### visited로 순열 구현
''' 희민프로님 주석
- 순열 : i(이전 선택) 필요 X -> v(방문 배열)만 필요
- 조합 : v (방문 배열) 필요 X -> i (이전 선택) 만 필요

※ 순서가 있는 조합은 순열이다 ex) 서로 다른 직원 3명 -> 일거리 3개
==> 일거리 3개를 뽑아서, 나열

N == 16 --> 가지치기 무조건 필요 (16^16)
'''


def dfs(curRow, curMultiply):
    global N, matrix, visited, maxMultiply
    # (D) 가지치기 -> 현재 곱이 max보다 작으면 가망없음 (<1)
    if curMultiply <= maxMultiply: # (D) =도 넣어서 뒤로 가기
        return

    # 종료조건
    if curRow == N:
        # print(curMultiply)
        if curMultiply > maxMultiply: # (D) 무조건 갱신하지 말기 -> 시간복잡도 관련
            maxMultiply = curMultiply
        return

    # 하부재귀
    for curCol in range(N):
        if not visited[curCol] and matrix[curRow][curCol] != 0:
            visited[curCol] = True
            dfs(curRow + 1, curMultiply * matrix[curRow][curCol] / 100)
            visited[curCol] = False


tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]

    maxMultiply = 0
    visited = [False] * N
    dfs(0, 1)
    print(f'#{i} {maxMultiply*100:.6f}')