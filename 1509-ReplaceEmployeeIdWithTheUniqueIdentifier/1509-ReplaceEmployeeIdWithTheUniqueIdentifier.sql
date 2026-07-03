-- Last updated: 7/3/2026, 12:46:20 PM
# Write your MySQL query statement below
select EmployeeUNI.unique_id,Employees.name 
from  Employees
left join EmployeeUNI on Employees.id=EmployeeUNI.id;
