## 해석: 수들의 합 5 - 슬라이딩 윈두르 형식

### ✨ 호심 아이디어

* 자연수 N을 1부터 시작하여 연속되는 자연수의 합으로 표현할 수 있는것을 검색
* 그러한 것을 활용해 가지수를 계산
* `start`와 `end`라는 두 포인터를 이용해 현재 개수 구간의 합을 관리
* 현재 합이 N보다 작으면 `end`를 증가, 크면 `start`를 증가

---

### 프로그램 (슬라이딩 윈두르)

```python
N = int(input())

start = 1
end = 1
current_sum = 1
count = 0

while start <= N: # 합은 1부터 시작, 연산하는 순서에 유의!!!
    if current_sum == N:
        count += 1
        current_sum -= start
        start += 1
    elif current_sum < N:
        end += 1
        current_sum += end
    else:
        current_sum -= start
        start += 1

print(count)
```

---

### 편병 동작 예시 (N = 15)

| start | end | current\_sum | 설명                           | count |
| ----- | --- | ------------ | ---------------------------- | ----- |
| 1     | 1   | 1            | current\_sum < 15 → end++    | 0     |
| 1     | 2   | 3            | current\_sum < 15 → end++    | 0     |
| 1     | 3   | 6            | current\_sum < 15 → end++    | 0     |
| 1     | 4   | 10           | current\_sum < 15 → end++    | 0     |
| 1     | 5   | 15           | current\_sum == 15 → count++ | 1     |
| 2     | 5   | 14           | current\_sum < 15 → end++    | 1     |
| 2     | 6   | 20           | current\_sum > 15 → start++  | 1     |
| 3     | 6   | 18           | current\_sum > 15 → start++  | 1     |
| 4     | 6   | 15           | current\_sum == 15 → count++ | 2     |
| 5     | 6   | 11           | current\_sum < 15 → end++    | 2     |
| 5     | 7   | 18           | current\_sum > 15 → start++  | 2     |
| 6     | 7   | 13           | current\_sum < 15 → end++    | 2     |
| 6     | 8   | 21           | current\_sum > 15 → start++  | 2     |
| 7     | 8   | 15           | current\_sum == 15 → count++ | 3     |
| 8     | 8   | 8            | current\_sum < 15 → end++    | 3     |
| 8     | 9   | 17           | current\_sum > 15 → start++  | 3     |
| 9     | 9   | 9            | current\_sum < 15 → end++    | 3     |
| 9     | 10  | 19           | current\_sum > 15 → start++  | 3     |
| 10    | 10  | 10           | current\_sum < 15 → end++    | 3     |
| 10    | 11  | 21           | current\_sum > 15 → start++  | 3     |
| 11    | 11  | 11           | current\_sum < 15 → end++    | 3     |
| 11    | 12  | 23           | current\_sum > 15 → start++  | 3     |
| 12    | 12  | 12           | current\_sum < 15 → end++    | 3     |
| 12    | 13  | 25           | current\_sum > 15 → start++  | 3     |
| 13    | 13  | 13           | current\_sum < 15 → end++    | 3     |
| 13    | 14  | 27           | current\_sum > 15 → start++  | 3     |
| 14    | 14  | 14           | current\_sum < 15 → end++    | 3     |
| 14    | 15  | 29           | current\_sum > 15 → start++  | 3     |
| 15    | 15  | 15           | current\_sum == 15 → count++ | 4     |

후적: 가지수 = **4**개

---

### 패턴 단어

* 현재 개수 구간의 합을 관리하며 가지수 계산
* 하나의 포인터만 일반적으로 증가/감소 해결
* 두 포인터가 각각 N까지 하나씩 이동 → **O(N)**
