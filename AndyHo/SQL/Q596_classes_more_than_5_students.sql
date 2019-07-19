# Write your MySQL query statement below

# using HAVING with DISTINCT
# 200 ms
# SELECT class
# FROM courses
# GROUP BY class
# HAVING COUNT( DISTINCT student ) >= 5;

# using GROUP BY with sub-query
# see Q182
# 193 ms
SELECT class
FROM (
    SELECT class, COUNT( DISTINCT student ) AS cnt
    FROM courses
    GROUP BY class
) AS tmp
WHERE cnt >= 5;