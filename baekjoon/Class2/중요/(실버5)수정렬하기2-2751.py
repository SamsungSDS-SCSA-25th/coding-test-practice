n = input()
numList = [ int(input()) for i in range(int(n)) ]

# 이중 for문 불가... 무엇을 써야할고?
for num in sorted(numList):
    print(num)