SELECT SUM(G.SCORE) AS SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES AS E JOIN HR_GRADE AS G ON E.EMP_NO = G.EMP_NO
GROUP BY G.EMP_NO
HAVING SUM(G.SCORE) = (
    SELECT MAX(TOTAL_SCORE)
    FROM (
        SELECT EMP_NO, SUM(SCORE) AS TOTAL_SCORE
        FROM HR_GRADE
        GROUP BY EMP_NO
    ) AS TOTAL_S
)