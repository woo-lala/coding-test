SELECT e3.id
FROM ECOLI_DATA e1 -- 1세대
JOIN ECOLI_DATA e2 ON e2.parent_id = e1.id -- 2세대
JOIN ECOLI_DATA e3 ON e3.parent_id = e2.id -- 3세대
WHERE e1.parent_id IS NULL
ORDER BY e3.id;

# WITH RECURSIVE Generation AS (
#     -- 앵커 파트: 1세대 개체
#     SELECT ID, PARENT_ID, 1 AS GENERATION
#     FROM ECOLI_DATA
#     WHERE PARENT_ID IS NULL

#     UNION ALL

#     -- 재귀 파트: 다음 세대 개체 찾기
#     SELECT E.ID, E.PARENT_ID, G.GENERATION + 1
#     FROM ECOLI_DATA AS E
#     JOIN Generation AS G ON E.PARENT_ID = G.ID
# )
# SELECT ID
# FROM Generation
# WHERE GENERATION = 3
# ORDER BY ID ASC;