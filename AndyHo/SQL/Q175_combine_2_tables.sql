# ref. https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/

# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;