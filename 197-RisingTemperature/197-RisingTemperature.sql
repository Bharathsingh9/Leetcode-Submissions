-- Last updated: 7/3/2026, 12:47:38 PM
SELECT today.id
FROM Weather yesterday 
CROSS JOIN Weather today
WHERE DATEDIFF(today.recordDate,yesterday.recordDate) = 1
    AND today.temperature > yesterday.temperature
;