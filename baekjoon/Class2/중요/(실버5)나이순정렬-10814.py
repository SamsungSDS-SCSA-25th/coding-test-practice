# 처음에는 사전형을 생각했으나 너무 구조가 복잡해짐...
# 결국 그냥 (age, name)을 순서대로 받는 것으로 구상

n = int(input())
ageNameList = [ tuple(input().split()) for i in range(n) ]

ageNameList.sort(key=lambda x: int(x[0]))

for age, name in ageNameList:
    print(age, name)