# 복도구간의 의미??
## 방 두개씩 청크단위로 생각
## 숨겨진 조건 찾기
# 결과적으로 필요한 시간 = “가장 많이 겹친(동시에 이동해야 하는) 구간”의 겹침 횟수

t = int(input())

for index in range(t):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    # print(matrix)
    duplicateCnt = 0
    corridorList = [0] * 201 # 1,2 / 3,4 / 5,6 / ... / 399,400 청크단위로 생각
    for roomInfo in matrix:
        start = (roomInfo[0] + 1) // 2 # (D) 방번호가 1인 경우 생각해서 1더함
        end = (roomInfo[1] + 1) // 2
        start, end = min(start, end), max(start, end) # (D) 방번호가 서로 뒤집힌 경우 -> 끝까지 생각 못함... (숨겨진 조건)
        for idx in range(start, end+1):
            corridorList[idx] += 1

    print(f'#{index+1} {max(corridorList)}')