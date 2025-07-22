switchN = int(input())
switchConditionList = list(map(int, input().split()))
studentN = int(input())
ruleMatrix = [ list(map(int, input().split())) for _ in range(studentN) ]

for rule in ruleMatrix:
    student, number = rule[0], rule[1]
    if student == 1: # 남자 -> 디버깅 완료
        for idx, switchCondition in enumerate(switchConditionList):
            #print(f'{idx=} {switchCondition=}')
            if (idx + 1) % number == 0:
                if switchCondition == 0:
                    switchConditionList[idx] = 1
                    #print(f'{switchConditionList=}')
                elif switchCondition == 1:
                    switchConditionList[idx] = 0
                    #print(f'{switchConditionList=}')
    elif student == 2: # 여자
        for prefix in range(number):
            if switchConditionList[number-1 - prefix] == switchConditionList[number-1 + prefix]:
                if switchConditionList[number-1 - prefix] == 0:
                    switchConditionList[number-1 - prefix] = 1
                    switchConditionList[number-1 + prefix] = 1
                elif switchConditionList[number-1 - prefix] == 1:
                    switchConditionList[number-1 - prefix] = 0
                    switchConditionList[number-1 + prefix] = 0


    #print(f'{switchConditionList=}')

# 열의 개수가 20인 2차원배열 만들어야함
for idx, switchCondition in enumerate(switchConditionList):
    print(switchCondition, end=' ')
    if (idx + 1) % 20 == 0:
        print()