# ref. https://leetcode.com/problems/rank-scores/

# Write your MySQL query statement below
SELECT
  Score,
  (
      SELECT COUNT(*)
      FROM
      (
          # find how many distinct value
          SELECT distinct Score AS s
          FROM Scores
      ) AS tmp
      # find the number of score >= current score (should be '>=' for ranking)
      WHERE s >= Score
  ) AS Rank
FROM Scores
ORDER BY Score desc
;