# Algorithm

### 알고리즘

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

<details close>
<summary><b>문자열</b></summary>
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
