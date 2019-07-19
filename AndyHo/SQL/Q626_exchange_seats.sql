# ref. https://dev.mysql.com/doc/refman/5.7/en/comparison-operators.html#function_coalesce

# Write your MySQL query statement below

# 1. CASE, 169 ms
# SELECT
# (
#     CASE
#         WHEN id % 2 != 0 AND id != counts THEN id + 1
#         WHEN id % 2 != 0 AND id = counts THEN id
#         ELSE id - 1
#     END
# ) AS id, student
# FROM
#     seat,
#     (
#         SELECT COUNT(*) AS counts
#         FROM seat
#     ) AS seat_counts
# ORDER BY id ASC;

# 2. BIT MANIPULATION, 155 ms
# SELECT *
# FROM
#     seat AS s1
#     LEFT JOIN
#         seat AS s2 ON (s1.id+1)^1-1 = s2.id
# ORDER BY s1.id;
#
## will generat the following table
# | id | student | id | student |
# |----|---------|----|---------|
# | 1  | Abbot   | 2  | Doris   |
# | 2  | Doris   | 1  | Abbot   |
# | 3  | Emerson | 4  | Green   |
# | 4  | Green   | 3  | Emerson |
# | 5  | Jeames  |    |         |
#
# the, use COALESCE() to get first non-null value for case id = 5 (s1 have value, but s2 no)
SELECT s1.id, COALESCE( s2.student, s1.student ) AS student
FROM
    seat AS s1
    LEFT JOIN
        seat AS s2 ON (s1.id+1)^1-1 = s2.id
ORDER BY s1.id
;

# COALESCE(): Returns the first non-NULL value in the list, or NULL if there are no non-NULL values.