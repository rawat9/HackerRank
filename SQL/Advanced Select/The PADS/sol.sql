SELECT name + '(' + LEFT(occupation, 1) + ')' FROM occupations
UNION
SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', lower(occupation), 's.') FROM occupations
GROUP BY occupation;