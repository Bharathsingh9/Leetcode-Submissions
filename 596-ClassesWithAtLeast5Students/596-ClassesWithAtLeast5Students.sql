-- Last updated: 7/3/2026, 12:47:04 PM
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;