# itertools의 조합 활용
# for문을 활용하면 중첩되는 반복이 많을 것 같음

from itertools import combinations

smurfList = [ int(input()) for _ in range(9) ]

for comb in list(combinations(smurfList, 7)):
    if sum(comb) == 100:
        for num in sorted(list(comb)):
            print(num)
        break