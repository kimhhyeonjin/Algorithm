-- 코드를 입력하세요
# COALESCE(A, B) : A가 NULL이 아닌 경우 A, A가 NULL인 경우 B 리턴
SELECT ANIMAL_TYPE, COALESCE(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID