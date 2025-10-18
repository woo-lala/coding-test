-- 코드를 입력하세요
SELECT n.flavor
FROM (
    SELECT f.flavor, f.TOTAL_ORDER
    FROM FIRST_HALF f

    UNION ALL

    SELECT j.flavor, SUM(j.TOTAL_ORDER)
    FROM JULY j
    GROUP BY j.flavor
) n
GROUP BY n.flavor
ORDER BY SUM(n.TOTAL_ORDER) DESC
LIMIT 3;