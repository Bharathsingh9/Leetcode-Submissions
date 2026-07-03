-- Last updated: 7/3/2026, 12:47:09 PM
# Write your MySQL query statement below
select a.name
from Employee a
inner join Employee b
where a.id=b.managerId 
group by a.id,a.name 
having count(*)>=5;
