SELECT a.name name_at, o.occurred_at time_occurred FROM
accounts a JOIN  orders o ON a.id = o.account_id;

SELECT a.name, AVG(o.standard_qty) avg_stand, AVG(o.gloss_qty) avg_gloss, AVG(o.poster_qty) avg_post
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;

select sr.id , sr.name , count(*) num_accounts
from accounts a 
join sales_reps  sr 
on sr.id =a.sales_rep_id
group by sr.id,sr.name
having count(*) > 5
order by num_accounts;

select a.id ,a.name , count(*) num_order 
from accounts a 
join orders o
on o.account_id = a.id
group by a.id, a.name
having count(*) > 20
order by num_order;

select a.id ,a.name , count(*) num_order 
from accounts a 
join orders o
on o.account_id = a.id
group by a.id, a.name
having count(*) > 20
order by num_order  desc limit 1;

select a.id ,a.name,sum(o.total_amt_usd) total_amt from accounts a 
join orders o
on o.account_id = a.id
group by a.id,a.name
having sum(o.total_amt_usd) > 300000
order by total_amt;


select a.id ,a.name,sum(o.total_amt_usd) total_amt from accounts a 
join orders o
on o.account_id = a.id
group by a.id,a.name
having sum(o.total_amt_usd) < 1000
order by total_amt;