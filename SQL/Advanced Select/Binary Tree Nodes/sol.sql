SELECT t1.N, 
    CASE WHEN t1.P IS NULL THEN 'Root'
    WHEN t1.N = t2.P THEN 'Inner'
    ELSE 'Leaf' END
    AS type
FROM BST t1
LEFT JOIN (SELECT DISTINCT(P) FROM BST) t2
ON t1.N = t2.P
ORDER BY 1;