SELECT * FROM orders; 
SELECT * FROM orders LIMIT 5; -- limit to 5
SELECT id ,name,website FROM accounts LIMIT 5; 
SELECT id ,account_id,occurred_at FROM orders;
SELECT occurred_at,account_id, channel FROM web_events LIMIT 15;
SELECT id,occurred_at,total_amt_usd FROM orders ORDER BY occurred_at LIMIT 10;
SELECT total_amt_usd , account_id ,total_amt_usd FROM orders ORDER BY  total_amt_usd DESC LIMIT 5;
SELECT id,account_id,total_amt_usd FROM orders ORDER BY total_amt_usd LIMIT 20;
SELECT id,account_id,total_amt_usd FROM orders ORDER BY account_id ASC,total_amt_usd ;
SELECT id,account_id,total_amt_usd FROM orders ORDER BY total_amt_usd DESC , account_id ASC ;
SELECT * FROM orders WHERE gloss_amt_usd >= 100 LIMIT 5;
SELECT * FROM orders WHERE total_amt_usd < 500 LIMIT 10;
SELECT name,website,primary_poc from accounts where name LIKE 'Exxon%' ;
SELECT name, website, primary_poc FROM accounts WHERE name = 'Exxon Mobil';
SELECT id,account_id, (standard_amt_usd/standard_qty) AS price_unit FROM orders LIMIT 10;
SELECT id, account_id, 
   poster_amt_usd/(standard_amt_usd + gloss_amt_usd + poster_amt_usd) AS post_per
FROM orders
LIMIT 10;

SELECT * FROM accounts WHERE name LIKE 'C%';
SELECT * FROM accounts WHERE name LIKE '%s';
SELECT * FROM accounts WHERE name LIKE '%one%';
SELECT name,primary_poc,sales_rep_id FROM accounts WHERE name IN ('Walmart','Target','Nordstrom') ;
SELECT * FROM web_events WHERE channel in ('organic','adwords');
SELECT * FROM web_events WHERE channel NOT IN ('organic','adwords');
SELECT name,primary_poc,sales_rep_id FROM account WHERE name NOT IN ('Walmart','Target','Nordstrom');

SELECT * FROM orders WHERE standard_qty > 1000 AND poster_qty <> 0 AND  gloss_qty = 0;
SELECT * FROM accounts WHERE name NOT LIKE 'C%' AND name NOT LIKE '%s';
SELECT * FROm orders WHERE gloss_qty BETWEEn 24 AND 29;
SELECT * FROM web_events WHERE channel IN ('organic','adwords') AND occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
ORDER BY occurred_at DESC ;
SELECT  orders.* FROM orders JOIN accounts ON orders.account_id = accounts.id;
SELECT * FROM orders JOIN accounts ON orders.account_id = accounts.id;
SELECT orders.standard_qty, orders.gloss_qty,orders.poster_qty,accounts.website,accounts.primary_poc FROM orders JOIN accounts ON orders.account_id = accounts.id;