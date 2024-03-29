SELECT t.CITY,
    t.ct
FROM (
        (
            SELECT TOP 1 CITY,
                LEN(CITY) as ct
            FROM STATION
            ORDER BY LEN(CITY) DESC,
                CITY DESC
        )
        union all
        (
            SELECT TOP 1 CITY,
                LEN(CITY) as ct
            FROM STATION
            ORDER BY LEN(CITY) asc,
                CITY asc
        )
    ) t