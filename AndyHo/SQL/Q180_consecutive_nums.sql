# Problem: Write a SQL query to find all numbers that appear at least three times consecutively.

# Write your MySQL query statement below
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM
    Logs AS l1,
    Logs AS l2,
    Logs AS l3
WHERE
    l1.Id = l2.Id - 1 AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l1.Num = l3.Num
;