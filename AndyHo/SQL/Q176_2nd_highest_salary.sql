# Write your MySQL query statement below

## [Problem] not able to return null if no row found
# However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table.
# 1. ------------------------------------------------------------
# SELECT IFNULL( Salary, null ) AS SecondHighestSalary
# FROM Employee
# # LIMIT OFFSET, COUNT
# ORDER BY Salary DESC LIMIT 1,1;

# 2. ------------------------------------------------------------
# SELECT DISTINCT
#     Salary AS SecondHighestSalary
# FROM
#     Employee
# ORDER BY Salary DESC
# LIMIT 1 OFFSET 1

# to solve the problem, treat it as a temp table
# SELECT
# (
#     SELECT Salary
#     FROM Employee
#     # LIMIT OFFSET, COUNT
#     ORDER BY Salary DESC LIMIT 1,1
# )  AS SecondHighestSalary
# ;

# IFNULL version
SELECT
    IFNULL(
        (
            SELECT DISTINCT Salary
            FROM Employee
            # LIMIT OFFSET, COUNT
            ORDER BY Salary DESC LIMIT 1,1
        ),
        NULL
    ) AS SecondHighestSalary
;