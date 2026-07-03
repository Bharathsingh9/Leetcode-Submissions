-- Last updated: 7/3/2026, 12:45:48 PM
# Write your MySQL query statement below
Select  teacher_id ,
count(distinct subject_id ) as cnt from Teacher
group by teacher_id