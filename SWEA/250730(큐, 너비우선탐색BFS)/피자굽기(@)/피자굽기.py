# 피자리스트를 만들때 Idx도 같이 저장해서 q를 돌려야함

from collections import deque

t = int(input())
for index in range(t):
    ovenSize, pizzaNum = map(int, input().split())
    cheezeList = list(map(int, input().split()))
    pizzaCheezeList = [ [pizzaIdx, cheeze] for pizzaIdx, cheeze in enumerate(cheezeList) ]
    q = deque(pizzaCheezeList[:ovenSize]) # 화덕의 사이즈 만큼 처음에 피자들어감
    pizzaCheezeList = pizzaCheezeList[ovenSize:] # 남은 피자리스트 갱신

    while True: # 맨 앞에서 확인하고 교체하는 피자 교체하는 작업필요
        if q[0][1] == 0: # 치즈가 0인 경우
            temp = q.popleft() # (D) 피자번호를 기억하고 있어야함... -> [idx, pizza]
            if pizzaCheezeList: # 피자리스트가 남아있으면
                q.appendleft(pizzaCheezeList.pop(0))
            elif not pizzaCheezeList and not q: # 피자리스트와 q 더이상 남은 것이 없다면
                answer = temp[0]+1
                break
        else: # 치즈가 남아 있는 경우
            q[0][1] //= 2
            q.rotate(-1)


    print(f'#{index+1} {answer}')