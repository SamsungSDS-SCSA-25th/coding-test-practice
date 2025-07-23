n = int(input())

result, flag = 0, False
for number in range(1, n):
    numberSum = 0
    for content in list(str(number)):
        #print(f'{content=}')
        numberSum += int(content)
    #print()
    maker = number + numberSum
    if n == maker:
        flag = True
        result = number
        break

if flag:
    print(result)
else:
    print(0)