SELECT CEIL(
        AVG(SALARY) - AVG(REPLACE(CAST(SALARY AS VARCHAR(100)), '0', ''))
    ) AS DIFF
FROM EMPLOYEES