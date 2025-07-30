````markdown
# Python `for-else` 문 정리

`for-else` 문은 `for` 루프가 **`break` 없이 정상적으로** 끝났을 때만 `else` 블록을 실행하는 독특한 구조입니다.

---

## 1. 기본 문법

```python
for 변수 in iterable:
    반복_수행_코드
    if 조건:
        break
else:
    # for 루프가 break 없이 마지막까지 모두 실행된 경우에만 실행
    else_수행_코드
````

* `for` 블록 내에서 `break`가 한 번이라도 실행되면 `else` 블록은 **실행되지 않습니다**.
* `for`가 iterable의 모든 요소를 끝까지 순회하고 `break`가 실행되지 않으면 `else` 블록이 **단 한 번** 실행됩니다.

---

## 2. 사용 시점

* **검사 후 후속 처리**가 필요할 때

  * 예: 리스트에서 특정 값을 찾고, 찾지 못했을 때만 별도 로직을 실행
* `flag` 변수를 사용하지 않고 코드가 더 깔끔해집니다.

---

## 3. 예시

### 예시 1: 소수 판별

```python
n = 29
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(f"{n}은(는) 소수가 아닙니다.")
        break
else:
    print(f"{n}은(는) 소수입니다.")
```

* `29`는 나눠지는 수가 없어 `break` 없이 루프 종료 → `else` 실행 → **소수**

### 예시 2: 리스트에서 값 검색

```python
fruits = ["apple", "banana", "cherry"]
target = "cherry"
for f in fruits:
    if f == target:
        print(f"발견: {target}")
        break
else:
    print(f"{target}은(는) 리스트에 없습니다.")
```

* `cherry`를 찾으면 `break` → `else` 미실행
* `orange` 같은 미존재 값이면 `else` 실행 → **리스트에 없음**

### 예시 3: 파일에서 키워드 검색

```python
lines = [
    "def foo():",
    "    pass",
    "# TODO: implement bar",
    "print('done')"
]
keyword = "TODO"
for idx, line in enumerate(lines, 1):
    if keyword in line:
        print(f"{idx}번째 줄에 {keyword} 발견!")
        break
else:
    print(f"{keyword}를 찾지 못했습니다.")
```

* `TODO`를 발견하면 `break` → `else` 미실행
* 발견 실패 시 `else` 실행

---

## 4. 요약

* `for-else`는 `break` 유무에 따라 후속 처리 분기
* 루프를 완전히 수행했을 때만 `else` 블록 실행
* 코드 가독성을 높이고 `flag` 사용을 줄여 줌

```
```
