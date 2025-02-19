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

  - 집계함수로 한 번에 하나의 집계 값을 반환하므로 MAX와 같은 함수와 함께 사용할 수 없음

    - [LV4 / HAVING절 / 그룹별 조건에 맞는 식당 목록 출력하기](./프로그래머스/4/131124. 그룹별 조건에 맞는 식당 목록 출력하기/그룹별 조건에 맞는 식당 목록 출력하기.sql)

    - 그룹화 후 최대값을 구하는 경우는 가능

- SUM

- AVG

- MAX

- MIN

- ROUND

  - 숫자 반올림

    ```mysql
    ROUND(값, 자릿수)
    -- 자릿수가 -1이면 1의 자리에서 반올림
    -- 자릿수가 0이면 소수점 첫째자리에서 반올림
    -- 자릿수가 1이면 소수점 둘째자리에서 반올림
    ```

    - [LV2 / SELECT절 / 노선별 평균 역 사이 거리 조회하기](./프로그래머스/2/284531. 노선별 평균 역 사이 거리 조회하기/노선별 평균 역 사이 거리 조회하기.sql)

- TRUNC

- CONCAT

  - 여러 문자열 혹은 컬럼값을 하나로 합쳐주는 역할

    ```mysql
    CONCAT(문자열1, 문자열2, 문자열3 ...)
    ```

    - [LV2 / SELECT절 / 노선별 평균 역 사이 거리 조회하기](./프로그래머스/2/284531. 노선별 평균 역 사이 거리 조회하기/노선별 평균 역 사이 거리 조회하기.sql)

- UPPER

- LOWER

- SUBSTRING

- NOW

- CURDATE

- DATEDIFF

</div>
</details>

<details close>
<summary><b>날짜 형식 변환</b></summary>
<div markdown="1">

- [LV4 / WHERE절 / 저자 별 카테고리 별 매출액 집계하기](./프로그래머스/4/144856. 저자 별 카테고리 별 매출액 집계하기/저자 별 카테고리 별 매출액 집계하기.sql)

</div>
</details>

<details close>
<summary><b>중복 제거 DISTINCT</b></summary>
<div markdown="1">

- [LV4 / SELECT절 / 년， 월， 성별 별 상품 구매 회원 수 구하기](./프로그래머스/4/131532. 년， 월， 성별 별 상품 구매 회원 수 구하기/년， 월， 성별 별 상품 구매 회원 수 구하기.sql)

- [LV4 / HAVING절 / 우유와 요거트가 담긴 장바구니](./프로그래머스/4/62284. 우유와 요거트가 담긴 장바구니/우유와 요거트가 담긴 장바구니.sql)

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

</div>
</details>

<details close>
<summary><b>서브쿼리</b></summary>
<div markdown="1">

- [LV2 / WHERE절 / 업그레이드 된 아이템 구하기](./프로그래머스/2/273711. 업그레이드 된 아이템 구하기/업그레이드 된 아이템 구하기.sql)

- [LV3 / WHERE절 / 헤비 유저가 소유한 장소](./프로그래머스/3/77487. 헤비 유저가 소유한 장소/헤비 유저가 소유한 장소.sql)

- [LV4 / WHERE절 / 그룹별 조건에 맞는 식당 목록 출력하기](./프로그래머스/4/131124. 그룹별 조건에 맞는 식당 목록 출력하기/그룹별 조건에 맞는 식당 목록 출력하기.sql)

</div>
</details>

<details close>
<summary><b>3중 JOIN문</b></summary>
<div markdown="1">

- [LV4 / FROM절 / 저자 별 카테고리 별 매출액 집계하기](./프로그래머스/4/144856. 저자 별 카테고리 별 매출액 집계하기/저자 별 카테고리 별 매출액 집계하기.sql)

</div>
</details>
