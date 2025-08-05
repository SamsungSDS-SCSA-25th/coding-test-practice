dayList1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 화수목금토일월 -> 순으로

n = int(input())
dayCnt, ansCnt = 0, 0
for year in range(2019, n+1):
    yoonFlag = False
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        yoonFlag = True

    for month in range(1, 13):
        if not yoonFlag:
            dayList = dayList1
        elif yoonFlag:
            dayList = dayList2

        for day in range(1, dayList[month]+1):
            # day를 누적하고 쌓아가면서 7로 나누었을 때 나머지가 1:화 / 2:수 / 3:목 / 4:금 / 5:토 / 6:일 / 0:월
            dayCnt += 1
            if day == 13 and dayCnt % 7 == 4:
                # print(f'{year=} {month=} {day=} {yoonFlag=}')
                ansCnt += 1

print(ansCnt)