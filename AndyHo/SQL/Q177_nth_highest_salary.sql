# ref. https://leetcode.com/problems/nth-highest-salary/discuss/53041/Accpted-Solution-for-the-Nth-Highest-Salary

## 1. Declare variable
# 273 ms
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N-1;
    RETURN (
        # Write your MySQL query statement below.
        SELECT DISTINCT Salary
        FROM Employee
        # LIMIT OFFSET, COUNT
        ORDER BY Salary DESC LIMIT M,1
    );
END

## 2. No need to declare variable, O(n^2)
# 595 ms
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        # Write your MySQL query statement below.
        SELECT DISTINCT e1.Salary
        FROM Employee AS e1
        # do the count for all the row to find the number of row < than it that is exactly N-1
        WHERE N-1 = (
            SELECT COUNT( DISTINCT e2.Salary )
            FROM Employee AS e2
            WHERE e1.Salary < e2.Salary
        )
    );
END
