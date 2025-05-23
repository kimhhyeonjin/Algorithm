WITH CHILD_DATA AS (
    SELECT PARENT_ID, COUNT(*) AS CHILD_COUNT
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NOT NULL
    GROUP BY PARENT_ID
)

SELECT E.ID, COALESCE(CHILD_COUNT, 0) AS CHILD_COUNT
FROM ECOLI_DATA AS E LEFT JOIN CHILD_DATA AS C ON E.ID = C.PARENT_ID