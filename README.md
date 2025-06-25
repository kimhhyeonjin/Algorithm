# Algorithm

### 알고리즘

<details close>
<summary><b>파이썬</b></summary>
<div markdown="1">

- 함수

  - map

    - 반복 가능한(iterable) 객체에 대해서 특정 함수를 적용하고 그 결과를 새로운 반복 가능한 객체로 반환하는 함수

    - map 객체 반환

      ```python
      map(function, iterable, ...)
      # function: 각 요소에 적용할 함수로 하나의 인자를 받는 함수여야 함
      # iterable: 함수가 적용될 반복 가능한 객체(리스트, 튜플, 문자열 등)
      # ...: 여러 개의 반복 가능한 객체를 전달할 수도 있습니다. 이 경우, 함수는 각 반복 가능한 객체에서 해당 인덱스의 값을 모두 인자로 받습니다.

      def add(x, y):
          return x + y

      numbers1 = [1, 2, 3]
      numbers2 = [4, 5, 6]

      result = map(add, numbers1, numbers2)

      print(list(result))  # [5, 7, 9]
      ```

      - [LV1 / 하샤드 수](./프로그래머스/1/12947. 하샤드 수/하샤드 수.py)

      - [LV2 / 튜플](./프로그래머스/2/64065. 튜플/튜플.py)

  - join

    - 문자열의 리스트나 튜플을 하나의 문자열로 합치는 함수

    - 문자열의 iterable 객체에서 사용해야 하므로, 숫자나 다른 데이터 타입을 문자열로 변환한 후에 사용

      ```python
      separator.join(iterable)

      fruits = ["apple", "banana", "cherry"]
      result = ", ".join(fruits)
      print(result)  # 출력: apple, banana, cherry
      ```

      - [LV1 / 정수 내림차순으로 배치하기](./프로그래머스/1/12933. 정수 내림차순으로 배치하기/정수 내림차순으로 배치하기.py)

  - sorted

    - 모든 iterable에 사용할 수 있는 함수로, 정렬된 새로운 리스트를 반환하며 원본 객체는 유지

      ```python
      new_list = sorted(list_name)
      new_list = sorted(list_name, reverse = True)
      new_list = sorted(list_name, key = lambda x : len(x), reverse = True)
      new_list = sorted(list_name, key = lambda x : (len(x), x), reverse = True)
      new_list = sorted(list_name, key = lambda x : (x[1], x[0]), reverse = True)
      ```

      - [LV1 / 문자열 내림차순으로 배치하기](./프로그래머스/1/12917. 문자열 내림차순으로 배치하기/문자열 내림차순으로 배치하기.py)

      - [LV1 / 문자열 내 마음대로 정렬하기](./프로그래머스/1/12915. 문자열 내 마음대로 정렬하기/문자열 내 마음대로 정렬하기.py)

- 리스트

  - 함수

    - sort

      - 원본을 변경하여 정렬

        ```python
        list_name.sort()
        list_name.sort(reverse = True)
        list_name.sort(key = lambda x : len(x), reverse = True)
        list_name.sort(key = lambda x : (len(x), x), reverse = True)
        list_name.sort(key = lambda x : (x[1], x[0]), reverse = True)
        ```

        - [LV2 / 튜플](./프로그래머스/2/64065. 튜플/튜플.py)

    - remove

      - 리스트에서 첫 번째로 나오는 값을 삭제하는 함수

        ```python
        a = [1, 2, 3, 1, 2, 3]
        a.remove(3)
        a   # [1, 2, 1, 2, 3]
        ```

    - count

      - 문자열이나 리스트 등에서 특정 요소의 개수를 세는 데 사용되는 함수

        ```python
        list_a = [1, 2, 5, 3, 6, 5, 1, 3, 1]
        cnt_a = list_a.count(1)
        print(cnt_a)    # 3
        ```

        - [LV2 / 이진 변환 반복하기](./프로그래머스/2/70129. 이진 변환 반복하기/이진 변환 반복하기.py)

    - [::-1]

      - 문자열, 리스트 등에서 문자열을 반대로 뒤집는 함수

- 딕셔너리

  - 원소 삭제하기

    ```python
    del dict_name['key_name']
    dict_name.pop('key_name')   # value 값 반환
    value = dict_name.pop('key_name')
    print(value)
    ```

    - [LV2 / 롤케이크 자르기](./프로그래머스/2/132265. 롤케이크 자르기/롤케이크 자르기.py)

- 숫자형

  - isdecimal

    - 문자열을 구성하는 각 원소가 0과 9사이의 정수(int)로 변환 가능한지 여부만을 판별

    - 숫자로 보이더라도 정수화가 불가능하면 False 반환

      ```python
      num.isdecimal()
      num.isdigit()
      num.isnumeric()
      ```

      - [LV1 / 문자열 다루기 기본](./프로그래머스/1/12918. 문자열 다루기 기본/문자열 다루기 기본.py)

  - 진수 변환

    - 10진수에서 2진수, 8진수, 16진수

      ```python
      bin(87)     # 0b1010111
      oct(87)     # 0o127
      hex(87)     # 0x57
      ```

      - [LV2 / 이진 변환 반복하기](./프로그래머스/2/70129. 이진 변환 반복하기/이진 변환 반복하기.py)

    - 2진수, 8진수, 16진수에서 10진수

      ```python
      int('0b1010111', 2)   # 87
      int('0o127', 8)       # 87
      int('0x57', 16)       # 87
      ```

    - n진수에서 10진수

      ```python
      int('n진수 문자열', n)
      int('101', 3)         # 10
      ```

- 문자열 자료형

  - f 문자열 포매팅 (f-string)

    - 문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수를 넣어 사용

      ```python
      name = "홍길동"
      age = 25
      greeting = f"안녕하세요, 제 이름은 {name}이고, 나이는 {age}입니다."
      print(greeting)
      ```

      - [LV1 / 서울에서 김서방 찾기](./프로그래머스/1/12919. 서울에서 김서방 찾기/서울에서 김서방 찾기.py)

  - 함수

    - upper

      - 대문자로 변환

        ```python
        a = 'hi'
        new_a = a.upper()
        print(new_a)    # 'HI'
        ```

        - [LV2 / JadenCase 문자열 만들기](./프로그래머스/2/12951. JadenCase 문자열 만들기/JadenCase 문자열 만들기.py)

    - lower

      - 소문자로 변환

        ```python
        a = 'HI'
        new_a = a.lower()
        print(new_a)    # 'hi'
        ```

        - [LV2 / JadenCase 문자열 만들기](./프로그래머스/2/12951. JadenCase 문자열 만들기/JadenCase 문자열 만들기.py)

    - isalpha

      - 문자열이 알파벳으로 구성되어 있는지 확인

      - 숫자나 공백이 포함되면 False 반환

        ```python
        print('ABC'.isalpha())        # True
        print('도레미'.isalpha())     # True
        print('A B C'.isalpha())      # False
        print('도레미123'.isalpha())  # False
        ```

    - isdigit

      - 문자열이 숫자로만 구성되어 있는지 확인

        ```python
        print('135'.isdigit())      # True
        print('1 3 5'.isdigit())    # False
        ```

    - replace

      - 문자열에서 특정 문자열을 다른 문자열로 교체

        ```python
        string.replace(old_value, new_value, count)       # count는 횟수 설정

        string = "Hello, world! world!!"
        new_string = string.replace("world", "Python")    # "Hello, Python! Python!!"
        new_string = string.replace("world", "Python", 1)    # "Hello, Python! world!!"
        ```

        - [LV1 / 숫자 문자열과 영단어](./프로그래머스/1/81301. 숫자 문자열과 영단어/숫자 문자열과 영단어.py)

        - [LV1 / 옹알이 （2）](./프로그래머스/1/133499. 옹알이 （2）/옹알이 （2）.py)

    - strip

      - 문자열 끝에서 특정 문자 제거

        ```python
        text.strip()            # 양쪽 공백 제거
        text.lstrip()           # 왼쪽 공백 제거
        text.tstrip()           # 오른쪽 공백 제거
        text.strip('x')         # 특정 문자 제거
        text.strip('xy')        # 여러 문자를 한 번에 제거 ('x', 'y'가 앞과 뒤에서 모두 제거)

        text = "xyxxyHello, World!yyx"
        stripped_text = text.strip('xy')
        print(stripped_text)  # 'Hello, World!'
        ```

        - [LV1 / 옹알이 （2）](./프로그래머스/1/133499. 옹알이 （2）/옹알이 （2）.py)

- 라이브러리

  - deque

    ```python
    from collections import deque
    d = deque()
    d.append([0, 0])
    i, j = d.popleft()
    ```

    - [LV2 / 게임 맵 최단거리](./프로그래머스/2/1844. 게임 맵 최단거리/게임 맵 최단거리.py)

  - defaultdict

    ```python
    from collections import defaultdict
    a = defaultdict(int)
    ```

    - [LV2 / 할인 행사](./프로그래머스/2/131127. 할인 행사/할인 행사.py)

  - combinations / permutations

    ```python
    from itertools import combinations
    from itertools import permutations

    c = list(combinations(iterable, r))
    p = list(permutations(iterable, r))
    ```

    - [LV2 / 피로도](./프로그래머스/2/87946. 피로도/피로도.py)

</div>
</details>

<details close>
<summary><b>완전탐색</b></summary>
<div markdown="1">

- [LV1 / 기사단원의 무기](./프로그래머스/1/136798. 기사단원의 무기/기사단원의 무기.py)

- [LV1 / 모의고사](./프로그래머스/1/42840. 모의고사/모의고사.py)

</div>
</details>

<details close>
<summary><b>그리디</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>구현</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>DFS</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>BFS</b></summary>
<div markdown="1">

- [LV2 / 게임 맵 최단거리](./프로그래머스/2/1844. 게임 맵 최단거리/게임 맵 최단거리.py)

</div>
</details>

<details close>
<summary><b>투포인터</b></summary>
<div markdown="1">

- [LV2 / 구명보트](./프로그래머스/2/42885. 구명보트/구명보트.py)

</div>
</details>

<details close>
<summary><b>정렬</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>이진 탐색</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>다이나믹 프로그래밍</b></summary>
<div markdown="1">

- [LV3 / 정수 삼각형](./프로그래머스/3/43105. 정수 삼각형/정수 삼각형.py)

</div>
</details>

<details close>
<summary><b>최단 경로</b></summary>
<div markdown="1">

</div>
</details>

<details close>
<summary><b>그래프 이론</b></summary>
<div markdown="1">

</div>
</details>

### SQL

- 기본 문법

  ```
  SELECT 열 이름
  FROM 테이블 이름
  WHERE 조건식
  GROUP BY 열 이름
  HAVING 조건식
  ORDER BY 열 이름
  LIMIT 숫자
  ```

- SELECT

<details close>
<summary><b>함수</b></summary>
<div markdown="1">

- COUNT

  - [LV2 / WHERE절 / 동명 동물 수 찾기](./프로그래머스/2/59041. 동명 동물 수 찾기/동명 동물 수 찾기.sql)

  - 집계함수로 한 번에 하나의 집계 값을 반환하므로 MAX와 같은 함수와 함께 사용할 수 없음

    - [LV4 / HAVING절 / 그룹별 조건에 맞는 식당 목록 출력하기](./프로그래머스/4/131124. 그룹별 조건에 맞는 식당 목록 출력하기/그룹별 조건에 맞는 식당 목록 출력하기.sql)

    - 그룹화 후 최대값을 구하는 경우는 가능

- SUM

  - [LV2 / SELECT절 / 조건에 맞는 아이템들의 가격의 총합 구하기](./프로그래머스/2/273709. 조건에 맞는 아이템들의 가격의 총합 구하기/조건에 맞는 아이템들의 가격의 총합 구하기.sql)

  - [LV4 / SELECT절 / 저자 별 카테고리 별 매출액 집계하기](./프로그래머스/4/144856. 저자 별 카테고리 별 매출액 집계하기/저자 별 카테고리 별 매출액 집계하기.sql)

  - [LV3 / SELECT절 / 자동차 대여 기록에서 대여중 ／ 대여 가능 여부 구분하기](./프로그래머스/3/157340. 자동차 대여 기록에서 대여중 ／ 대여 가능 여부 구분하기/자동차 대여 기록에서 대여중 ／ 대여 가능 여부 구분하기.sql)

  - 집계함수로 한 번에 하나의 집계 값을 반환하므로 MAX와 같은 함수와 함께 사용할 수 없음

    - [LV2 / HAVING절 / 조건에 맞는 사원 정보 조회하기](./프로그래머스/2/284527. 조건에 맞는 사원 정보 조회하기/조건에 맞는 사원 정보 조회하기.sql)

    - 그룹화 후 최대값을 구하는 경우는 가능

- AVG

- MAX

  - [LV1 / SELECT절 / 가장 비싼 상품 구하기](./프로그래머스/1/131697. 가장 비싼 상품 구하기/가장 비싼 상품 구하기.sql)

  - [LV1 / SELECT절 / 최댓값 구하기](./프로그래머스/1/59415. 최댓값 구하기/최댓값 구하기.sql)

- MIN

  - [LV2 / SELECT절 / 최솟값 구하기](./프로그래머스/2/59038. 최솟값 구하기/최솟값 구하기.sql)

- ROUND

  - 숫자 반올림

    ```mysql
    ROUND(값, 자릿수)
    -- 자릿수가 -1이면 1의 자리에서 반올림
    -- 자릿수가 0이면 소수점 첫째자리에서 반올림
    -- 자릿수가 1이면 소수점 둘째자리에서 반올림
    ```

    - [LV2 / SELECT절 / 노선별 평균 역 사이 거리 조회하기](./프로그래머스/2/284531. 노선별 평균 역 사이 거리 조회하기/노선별 평균 역 사이 거리 조회하기.sql)

    - [LV1 / SELECT절 / 평균 일일 대여 요금 구하기](./프로그래머스/1/151136. 평균 일일 대여 요금 구하기/평균 일일 대여 요금 구하기.sql)

- TRUNCATE

  - 반올림 없이 내림

    ```mysql
    TRUNCATE(값, 자릿수)
    -- 자릿수가 -1이면 10의 단위 정수
    -- 자릿수가 0이면 결과는 정수
    -- 자릿수가 1이면 소수점 첫째자리에서 내림
    ```

- FLOOR

  - 숫자보다 작거나 같은 가장 큰 정수(내림)

    ```mysql
    FLOOR(값)
    SELECT FLOOR(123.4567);  -- 결과: 123
    SELECT FLOOR(123.9999);  -- 결과: 123
    SELECT FLOOR(-123.4567); -- 결과: -124
    ```

- CEIL

  - 숫자보다 크거나 같은 가장 작은 정수(올림)

    ```mysql
    CEIL(값)
    SELECT CEIL(123.4567);  -- 결과: 124
    SELECT CEIL(123.9999);  -- 결과: 124
    SELECT CEIL(-123.4567); -- 결과: -123
    ```

- CONCAT

  - 여러 문자열 혹은 컬럼값을 하나로 합쳐주는 역할

    ```mysql
    CONCAT(문자열1, 문자열2, 문자열3 ...)
    ```

    - [LV2 / SELECT절 / 노선별 평균 역 사이 거리 조회하기](./프로그래머스/2/284531. 노선별 평균 역 사이 거리 조회하기/노선별 평균 역 사이 거리 조회하기.sql)

    - [LV3 / SELECT절 / 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기](./프로그래머스/3/164671. 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기/조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기.sql)

- UPPER

- LOWER

- SUBSTRING

  - 문자열의 일부분을 추출하는데 사용

    ```mysql
    SUBSTRING(문자열, 시작위치, 길이)
    ```

    - [LV3 / SELECT절 / 조건에 맞는 사용자 정보 조회하기](./프로그래머스/3/164670. 조건에 맞는 사용자 정보 조회하기/조건에 맞는 사용자 정보 조회하기.sql)

- NOW

- CURDATE

- DATEDIFF

  - 두 날짜 사이의 차이를 계산하는 함수

    ```mysql
    DATEDIFF(date1, date2)
    -- (date1 - date2) 값 반환
    -- date1과 date2 사이의 차이를 일 단위로 반환
    ```

    - [LV3 / ORDER BY절 / 오랜 기간 보호한 동물（2）](./프로그래머스/3/59411. 오랜 기간 보호한 동물（2）/오랜 기간 보호한 동물（2）.sql)

    - [LV1 / SELECT절 / 자동차 대여 기록에서 장기／단기 대여 구분하기](./프로그래머스/1/151138. 자동차 대여 기록에서 장기／단기 대여 구분하기/자동차 대여 기록에서 장기／단기 대여 구분하기.sql)

    - [LV2 / SELECT절 / 자동차 평균 대여 기간 구하기](./프로그래머스/2/157342. 자동차 평균 대여 기간 구하기/자동차 평균 대여 기간 구하기.sql)

- NTILE

  - 데이터를 지정한 수의 구간으로 나누고, 각 데이터에 구간 번호를 할당하는 함수

    ```mysql
    NTILE(num_buckets) OVER (PARTITION BY column ORDER BY column)
    ```

    - num_buckets

      - 데이터를 나누고자 하는 구간의 수

      - 4로 설정하면 데이터를 4개의 구간으로 나누고, 각 데이터에 1, 2, 3, 4 중 하나의 값을 할당

    - PARTITION BY(선택적)

      - 데이터를 구간을 나누기 전에 특정 컬럼을 기준으로 그룹화

      - 생략하면 전체 데이터를 기준으로 나눔

    - ORDER BY

      - 데이터를 어떤 기준으로 정렬할지 결정

    - [LV3 / SELECT절 / 대장균의 크기에 따라 분류하기 2](./프로그래머스/3/301649. 대장균의 크기에 따라 분류하기 2/대장균의 크기에 따라 분류하기 2.sql)

</div>
</details>

<details close>
<summary><b>날짜 형식 변환</b></summary>
<div markdown="1">

- DATE_FORMAT

  - [LV4 / WHERE절 / 저자 별 카테고리 별 매출액 집계하기](./프로그래머스/4/144856. 저자 별 카테고리 별 매출액 집계하기/저자 별 카테고리 별 매출액 집계하기.sql)

  - [LV2 / SELECT절 / DATETIME에서 DATE로 형 변환](./프로그래머스/2/59414. DATETIME에서 DATE로 형 변환/DATETIME에서 DATE로 형 변환.sql)

  - DATE_FORMAT(NULL, '%Y-%m-%d') -> NULL 반환

    - [LV3 / SELECT절 / 조건별로 분류하여 주문상태 출력하기](./프로그래머스/3/131113. 조건별로 분류하여 주문상태 출력하기/조건별로 분류하여 주문상태 출력하기.sql)

</div>
</details>

<details close>
<summary><b>BETWEEN A AND B</b></summary>
<div markdown="1">

- A값과 B값 모두 포함

- [LV3 / WHERE절 / 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기](./프로그래머스/3/151139. 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기/대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기.sql)

- [LV1 / WHERE절 / 조건에 맞는 회원수 구하기](./프로그래머스/1/131535. 조건에 맞는 회원수 구하기/조건에 맞는 회원수 구하기.sql)

- [LV2 / WHERE절 / 입양 시각 구하기（1）](./프로그래머스/2/59412. 입양 시각 구하기（1）/입양 시각 구하기（1）.sql)

</div>
</details>

<details close>
<summary><b>LIKE</b></summary>
<div markdown="1">

- 특정 패턴을 열에서 검색하는 데 사용

  ```mysql
  SELECT 열 이름
  FROM 테이블 이름
  WHERE 열 이름 LIKE 패턴;
  ```

  - 와일드카드

    - %

      - 0개 이상의 문자와 일치

    - \_

      - 정확히 한 문자와 일치

- [LV1 / WHERE절 / 강원도에 위치한 생산공장 목록 출력하기](./프로그래머스/1/131112. 강원도에 위치한 생산공장 목록 출력하기/강원도에 위치한 생산공장 목록 출력하기.sql)

- [LV2 / WHERE절 / 이름에 el이 들어가는 동물 찾기](./프로그래머스/2/59047. 이름에 el이 들어가는 동물 찾기/이름에 el이 들어가는 동물 찾기.sql)

- [LV2 / WHERE절 / 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기](./프로그래머스/2/151137. 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기/자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기.sql)

- [LV4 / WHERE절 / 보호소에서 중성화한 동물](./프로그래머스/4/59045. 보호소에서 중성화한 동물/보호소에서 중성화한 동물.sql)

</div>
</details>

<details close>
<summary><b>중복 제거 DISTINCT</b></summary>
<div markdown="1">

- [LV4 / SELECT절 / 년， 월， 성별 별 상품 구매 회원 수 구하기](./프로그래머스/4/131532. 년， 월， 성별 별 상품 구매 회원 수 구하기/년， 월， 성별 별 상품 구매 회원 수 구하기.sql)

- [LV4 / HAVING절 / 우유와 요거트가 담긴 장바구니](./프로그래머스/4/62284. 우유와 요거트가 담긴 장바구니/우유와 요거트가 담긴 장바구니.sql)

- [LV2 / SELECT절 / 중복 제거하기](./프로그래머스/2/59408. 중복 제거하기/중복 제거하기.sql)

</div>
</details>

<details close>
<summary><b>조건문 IF</b></summary>
<div markdown="1">

```mysql
IF(조건, 조건을 만족할 때 결과, 조건을 만족하지 않을 때 결과)
```

- [LV2 / SELECT절 / 중성화 여부 파악하기](./프로그래머스/2/59409. 중성화 여부 파악하기/중성화 여부 파악하기.sql)

</div>
</details>

<details close>
<summary><b>조건문 CASE WHEN</b></summary>
<div markdown="1">

```mysql
CASE WHEN 조건1 THEN '조건1을 만족할 때 결과'
     WHEN 조건2 THEN '조건2를 만족할 때 결과'
     ...
     ELSE '위 조건을 모두 만족하지 않을 때 결과'
END
```

- [LV3 / HAVING절 / 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기](./프로그래머스/3/298519. 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기/특정 조건을 만족하는 물고기별 수와 최대 길이 구하기.sql)

- [LV2 / SELECT절 / NULL 처리하기](./프로그래머스/2/59410. NULL 처리하기/NULL 처리하기.sql)

- [LV1 / SELECT절 / 경기도에 위치한 식품창고 목록 출력하기](./프로그래머스/1/131114. 경기도에 위치한 식품창고 목록 출력하기/경기도에 위치한 식품창고 목록 출력하기.sql)

- [LV2 / SELECT절 / 중성화 여부 파악하기](./프로그래머스/2/59409. 중성화 여부 파악하기/중성화 여부 파악하기.sql)

- [LV3 / SELECT절 / 조건별로 분류하여 주문상태 출력하기](./프로그래머스/3/131113. 조건별로 분류하여 주문상태 출력하기/조건별로 분류하여 주문상태 출력하기.sql)

- [LV3 / SELECT절 / 대장균의 크기에 따라 분류하기 1](./프로그래머스/3/299307. 대장균의 크기에 따라 분류하기 1/대장균의 크기에 따라 분류하기 1.sql)

- [LV2 / SELECT절 / 조건에 부합하는 중고거래 상태 조회하기](./프로그래머스/2/164672. 조건에 부합하는 중고거래 상태 조회하기/조건에 부합하는 중고거래 상태 조회하기.sql)

- [LV4 / SELECT절 / 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기](./프로그래머스/4/284528. 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기/연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기.sql)

</div>
</details>

<details close>
<summary><b>NULL</b></summary>
<div markdown="1">

- IS NULL

  - [LV1 / WHERE절 / 이름이 없는 동물의 아이디](./프로그래머스/1/59039. 이름이 없는 동물의 아이디/이름이 없는 동물의 아이디.sql)

  - [LV1 / WHERE절 / 잔챙이 잡은 수 구하기](./프로그래머스/1/293258. 잔챙이 잡은 수 구하기/잔챙이 잡은 수 구하기.sql)

  - [LV2 / WHERE절 / ROOT 아이템 구하기](./프로그래머스/2/273710. ROOT 아이템 구하기/ROOT 아이템 구하기.sql)

- IS NOT NULL

  - [LV2 / WHERE절 / 동명 동물 수 찾기](./프로그래머스/2/59041. 동명 동물 수 찾기/동명 동물 수 찾기.sql)

  - [LV2 / WHERE절 / 3월에 태어난 여성 회원 목록 출력하기](./프로그래머스/2/131120. 3월에 태어난 여성 회원 목록 출력하기/3월에 태어난 여성 회원 목록 출력하기.sql)

  - NOT IN NULL 사용하면 FALSE값 반환

    - [LV3 / WHERE절 / 업그레이드 할 수 없는 아이템 구하기](./프로그래머스/3/273712. 업그레이드 할 수 없는 아이템 구하기/업그레이드 할 수 없는 아이템 구하기.sql)

- IFNULL

  ```mysql
  IFNULL(Column, "대체값")
  ```

  - Column이 NULL일 때 대체값으로 대체

  - [LV2 / SELECT절 / NULL 처리하기](./프로그래머스/2/59410. NULL 처리하기/NULL 처리하기.sql)

- COALESCE

  - NULL이 아닌 첫번째 값 (모든 데이터베이스에서 사용)

    ```mysql
    COALESCE(Column1, Column2, Column3, ...)
    ```

    - 전부 NULL값이라면 NULL 반환

    - [LV2 / SELECT절 / NULL 처리하기](./프로그래머스/2/59410. NULL 처리하기/NULL 처리하기.sql)

    - [LV1 / SELECT절 / 경기도에 위치한 식품창고 목록 출력하기](./프로그래머스/1/131114. 경기도에 위치한 식품창고 목록 출력하기/경기도에 위치한 식품창고 목록 출력하기.sql)

    - [LV1 / SELECT절 / 12세 이하인 여자 환자 목록 출력하기](./프로그래머스/1/132201. 12세 이하인 여자 환자 목록 출력하기/12세 이하인 여자 환자 목록 출력하기.sql)

    - [LV1 / SELECT절 / 잡은 물고기의 평균 길이 구하기](./프로그래머스/1/293259. 잡은 물고기의 평균 길이 구하기/잡은 물고기의 평균 길이 구하기.sql)

</div>
</details>

<details close>
<summary><b>서브쿼리</b></summary>
<div markdown="1">

- [LV2 / WHERE절 / 업그레이드 된 아이템 구하기](./프로그래머스/2/273711. 업그레이드 된 아이템 구하기/업그레이드 된 아이템 구하기.sql)

- [LV3 / WHERE절 / 헤비 유저가 소유한 장소](./프로그래머스/3/77487. 헤비 유저가 소유한 장소/헤비 유저가 소유한 장소.sql)

- [LV4 / WHERE절 / 그룹별 조건에 맞는 식당 목록 출력하기](./프로그래머스/4/131124. 그룹별 조건에 맞는 식당 목록 출력하기/그룹별 조건에 맞는 식당 목록 출력하기.sql)

- [LV2 / WHERE절 / 가격이 제일 비싼 식품의 정보 출력하기](./프로그래머스/2/131115. 가격이 제일 비싼 식품의 정보 출력하기/가격이 제일 비싼 식품의 정보 출력하기.sql)

</div>
</details>

<details close>
<summary><b>3중 JOIN문</b></summary>
<div markdown="1">

- [LV4 / FROM절 / 저자 별 카테고리 별 매출액 집계하기](./프로그래머스/4/144856. 저자 별 카테고리 별 매출액 집계하기/저자 별 카테고리 별 매출액 집계하기.sql)

</div>
</details>

<details close>
<summary><b>집합</b></summary>
<div markdown="1">

- 합집합 (UNION)

  - UNION

    - 중복된 값을 제거하고 결과 반환

      ```mysql
      SELECT column_name FROM table1
      UNION
      SELECT column_name FROM table2;
      ```

      - [LV4 / UNION / 오프라인／온라인 판매 데이터 통합하기](./프로그래머스/4/131537. 오프라인／온라인 판매 데이터 통합하기/오프라인／온라인 판매 데이터 통합하기.sql)

  - UNION ALL

    - 중복된 값도 포함하여 결과 반환

      ```mysql
      SELECT column_name FROM table1
      UNION ALL
      SELECT column_name FROM table2;
      ```

- 교집합 (INTERSECT)

  - INNER JOIN

    ```mysql
    SELECT column_name FROM table1
    INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```

    - [LV4 / FROM절 / 식품분류별 가장 비싼 식품의 정보 조회하기](./프로그래머스/4/131116. 식품분류별 가장 비싼 식품의 정보 조회하기/식품분류별 가장 비싼 식품의 정보 조회하기.sql)

  - EXISTS

    ```mysql
    SELECT column_name
    FROM table1 t1
    WHERE EXISTS (SELECT 1 FROM table2 t2 WHERE t1.column_name = t2.column_name);
    ```

- 차집합 (DIFFERENCE 또는 EXCEPT)

  - LEFT JOIN

    ```mysql
    SELECT column_name FROM table1
    LEFT JOIN table2 ON table1.column_name = table2.column_name
    WHERE table2.column_name IS NULL;
    ```

    - [LV3 / WHERE절 / 오랜 기간 보호한 동물（1）](./프로그래머스/3/59044. 오랜 기간 보호한 동물（1）/오랜 기간 보호한 동물（1）.sql)

    - [LV3 / WHERE절 / 없어진 기록 찾기](./프로그래머스/3/59042. 없어진 기록 찾기/없어진 기록 찾기.sql)

    - [LV4 / FROM절 / 주문량이 많은 아이스크림들 조회하기](./프로그래머스/4/133027. 주문량이 많은 아이스크림들 조회하기/주문량이 많은 아이스크림들 조회하기.sql)

    - [LV4 / FROM절 / 입양 시각 구하기（2）](./프로그래머스/4/59413. 입양 시각 구하기（2）/입양 시각 구하기（2）.sql)

- 대칭차집합 (XOR)

  - LEFT JOIN과 RIGHT JOIN 조합

    ```mysql
    SELECT column_name FROM table1
    LEFT JOIN table2 ON table1.column_name = table2.column_name
    WHERE table2.column_name IS NULL
    UNION
    SELECT column_name FROM table2
    LEFT JOIN table1 ON table2.column_name = table1.column_name
    WHERE table1.column_name IS NULL;
    ```

</div>
</details>

<details close>
<summary><b>CTE(Common Table Expression)</b></summary>
<div markdown="1">

- 복잡한 쿼리를 더 읽기 쉽게 만들고 재사용할 수 있도록 해주는 기능

  ```mysql
  WITH cte_name AS (
      -- CTE 정의: 서브쿼리나 SELECT문 등
      SELECT column1, column2
      FROM table_name
      WHERE condition
  )
  -- CTE를 활용한 메인 쿼리
  SELECT * FROM cte_name;
  ```

- WITH

  - [LV3 / WITH / 대장균들의 자식의 수 구하기](./프로그래머스/3/299305. 대장균들의 자식의 수 구하기/대장균들의 자식의 수 구하기.sql)

  - [LV4 / WITH / 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기](./프로그래머스/4/284528. 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기/연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기.sql)

  - [LV2 / WITH / 연도별 대장균 크기의 편차 구하기](./프로그래머스/2/299310. 연도별 대장균 크기의 편차 구하기/연도별 대장균 크기의 편차 구하기.sql)

- WITH RECURSIVE

  - [LV4 / WITH RECURSIVE / 입양 시각 구하기（2）](./프로그래머스/4/59413. 입양 시각 구하기（2）/입양 시각 구하기（2）.sql)

</div>
</details>
