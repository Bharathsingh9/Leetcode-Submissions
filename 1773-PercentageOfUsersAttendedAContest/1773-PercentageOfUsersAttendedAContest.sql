-- Last updated: 7/3/2026, 12:46:07 PM
# Write your MySQL query statement below
SELECT
    contest_id,
    ROUND(
        (COUNT(user_id) / (SELECT COUNT(1) FROM Users) * 100),
        2
    ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id