# Problem: Write a SQL query to find employees who earn the top three salaries in each of the department.

# Write your MySQL query statement below
SELECT
    d.Name  AS 'Department',
    e1.Name AS 'Employee',
    e1.Salary
FROM
    Employee e1
    JOIN Department AS d ON e1.DepartmentId = d.id
WHERE
    3 > (
        # here will return a number!!
        SELECT
            COUNT( DISTINCT e2.Salary )
        FROM Employee AS e2
        WHERE
            e2.Salary > e1.Salary
            # this condition do the counts for each department
            AND e1.DepartmentId = e2.DepartmentId
    )
;

# Example: Top 3 salary in the company

# select e1.Name as 'Employee', e1.Salary
# from Employee e1
# where 3 >
# (
#     select count(distinct e2.Salary)
#     from Employee e2
#     where e2.Salary > e1.Salary
# )
# ;

# Return:
# | Employee | Salary |
# |----------|--------|
# | Henry    | 80000  |
# | Max      | 90000  |
# | Randy    | 85000  |