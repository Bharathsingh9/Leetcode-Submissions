-- Last updated: 7/3/2026, 12:46:11 PM
# Write your MySQL query statement below
select a.customer_id,count(*) as count_no_trans
from visits a
left join Transactions b
on a.visit_id=b.visit_id
where b.transaction_id is null
group by a.customer_id;

