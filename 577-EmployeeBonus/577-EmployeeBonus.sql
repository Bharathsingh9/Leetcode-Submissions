-- Last updated: 7/3/2026, 12:47:07 PM
select e.name,b.bonus 
from Employee e
left join Bonus b
on e.empid=b.empid
where bonus<1000 or b.bonus is null;

