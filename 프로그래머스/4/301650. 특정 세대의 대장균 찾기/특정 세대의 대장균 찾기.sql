SELECT e3.id
FROM ECOLI_DATA e1 -- 1세대
JOIN ECOLI_DATA e2 ON e2.parent_id = e1.id -- 2세대
JOIN ECOLI_DATA e3 ON e3.parent_id = e2.id -- 3세대
WHERE e1.parent_id IS NULL
ORDER BY e3.id;