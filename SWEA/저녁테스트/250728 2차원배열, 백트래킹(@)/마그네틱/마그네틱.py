# 풀이시간: 약 40분
# 전치행렬로 풀이

t = 10

for index in range(t):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    matrixT = list(map(list, zip(*matrix)))

    stickCnt = 0
    for rowList in matrixT:
        tempList = []
        # print(f'{rowList=}')
        for val in rowList:
            # 0이 아니면 넣기
            if val != 0:
                tempList.append(val)

        # print(f'{tempList=}')
        # 12가 붙어있으면 하나의 교착상태
        # 2개씩 윈도우를 넣어서 12 몇개인지 확인
        for idx in range(len(tempList)-1):
            if tempList[idx] == 1 and  tempList[idx+1] == 2:
                stickCnt += 1

    print(f'#{index+1} {stickCnt}')