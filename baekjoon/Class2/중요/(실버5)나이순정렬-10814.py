# 사전을 사용하여 나이순으로 정렬하면, values 순으로 출력하도록함

n = int(input())
memberList = [ list(input().split()) for i in range(n) ]

ageNameDict = {}
for age, name in memberList:
    ageNameDict.setdefault(int(age), []).append(name)

ageNameList = [ []* ]
for age, name in ageNameDict.items():
    ageNameList.append(age)
    ageNameList.append(name)

print(ageNameList)
#ageNameList.sort()
#print(*ageNameList)