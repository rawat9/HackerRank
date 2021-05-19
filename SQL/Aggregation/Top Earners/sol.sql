SELECT * FROM 
(SELECT salary*months as earning, COUNT(*) as t FROM employee
GROUP BY salary*months) z
WHERE t=7
