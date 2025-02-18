-- 코드를 입력하세요
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M JOIN REST_REVIEW AS R ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID IN (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(REVIEW_ID) = (
        SELECT MAX(RI)
        FROM (
            -- AS RI를 해줘야 SELECT절에서 MAX를 정확하게 구할 수 있음
            SELECT COUNT(REVIEW_ID) AS RI
            FROM REST_REVIEW
            GROUP BY MEMBER_ID
            -- AS C를 입력하지 않으면 'Every derived table must have its own alias' 에러 발생
            ) AS C
    )
)
ORDER BY REVIEW_DATE, REVIEW_TEXT