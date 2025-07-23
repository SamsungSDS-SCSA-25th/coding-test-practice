while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    sortList = sorted([a, b, c], reverse=True)
    #print(sortList)
    if sortList[0]**2  == (sortList[1]**2 + sortList[2]**2):
        print('right')
    else:
        print('wrong')