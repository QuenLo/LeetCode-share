# ref. [DATEDIFF EXAMPLE] https://www.w3schools.com/sql/func_mysql_datediff.asp
# The DATEDIFF() function returns the number of days between two date values.

# Write your MySQL query statement below
SELECT weather.Id AS 'Id'
FROM weather
    JOIN weather AS w
    # The DATEDIFF() function returns the number of days between two date values
    ON DATEDIFF( weather.RecordDate, w.RecordDate ) = 1
    AND weather.Temperature > w.Temperature
;

