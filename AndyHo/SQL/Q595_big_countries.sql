# ref. https://leetcode.com/problems/big-countries/discuss/103561/Union-and-OR-and-the-Explanation

# OR
# SELECT name, population, area FROM World WHERE population > 25000000 OR area > 3000000;

# UNION
SELECT name, population, area
FROM World
WHERE area > 3000000 

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000;