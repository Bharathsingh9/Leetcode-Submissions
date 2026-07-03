-- Last updated: 7/3/2026, 12:47:03 PM
# Write your MySQL query statement below
select id,movie,description,rating 
from Cinema
where id%2=1 and description != "boring" order by rating desc;