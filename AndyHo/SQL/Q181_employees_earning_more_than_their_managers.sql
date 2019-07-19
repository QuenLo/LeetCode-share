# using WHERE
# 501 ms
# SELECT a.Name AS 'Employee'
# # create 2 tmp table
# FROM
#     Employee AS a,
#     Employee AS b
# WHERE
#     a.ManagerId = b.Id
#     AND a.Salary > b.Salary
# ;

# using JOIN
# 315 ms
SELECT a.NAME AS Employee
FROM Employee AS a
JOIN Employee AS b
    ON a.ManagerId = b.Id
        AND a.Salary > b.Salary
;
