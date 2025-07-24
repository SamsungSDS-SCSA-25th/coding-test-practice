for index in range(1,11):

    n = int(input())
    buildingList = list(map(int, input().split()))

    cnt = 0
    for building in range(2, n-2): # 이웃 4군데와의 차가 모두 양수이면 조망권 확보
        for floor in range(1, buildingList[building]+1):
            if floor > buildingList[building - 2] and floor > buildingList[building - 1] and floor > buildingList[building + 1] and floor > buildingList[building + 2]:
                cnt += 1

    print(f'#{index} {cnt}')