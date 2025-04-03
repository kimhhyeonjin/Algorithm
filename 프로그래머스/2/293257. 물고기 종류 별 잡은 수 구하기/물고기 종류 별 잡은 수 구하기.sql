SELECT COUNT(*) AS FISH_COUNT, FNI.FISH_NAME
FROM FISH_INFO AS FI JOIN FISH_NAME_INFO AS FNI ON FI.FISH_TYPE = FNI.FISH_TYPE
GROUP BY FNI.FISH_NAME
ORDER BY FISH_COUNT DESC