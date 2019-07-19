# ref. http://www.mysqltutorial.org/sql-in.aspx

# Write your MySQL query statement below
SELECT
    Department.Name AS 'Department',
    Employee.Name   AS 'Employee',
    Salary
FROM
    Employee
    JOIN
        Department ON Employee.DepartmentId = Department.Id
WHERE
    ( Employee.DepartmentId, Salary )
    IN
    (
        SELECT DepartmentId, MAX( Salary ) AS Salary
        FROM Employee
        GROUP BY DepartmentId
    )
;
# (A1, B1) IN (A2, B2) -> find row that A1 == A2, B1 == B2