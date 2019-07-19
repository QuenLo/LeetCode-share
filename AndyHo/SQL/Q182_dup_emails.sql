# GROUP BY w/ tmp table
# select form the tmp table 'tmp'
# 158 ms
SELECT Email FROM
(
    # create the temporary table
    SELECT Email, count( Email ) AS cnt
    FROM Person
    GROUP BY Email
) AS tmp
WHERE cnt > 1;

# HAVING
# 196 ms
# SELECT Email
# FROM Person
# GROUP BY Email
# HAVING count(Email) > 1;