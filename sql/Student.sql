CREATE DATABASE IF NOT EXISTS Company_DB;
-- createdb -U <username> -h <localhost> -p <port> -E <encoding> -T <template0> <database_name>
-- the above command will create & connect a database with the name student_db 
-- with the encoding utf8 and template0 as the template
-- the -T option is optional
CREATE SCHEMA IF NOT EXISTS com;

CREATE TABLE IF NOT EXISTS Company_DB.com.Company (
    id INT PRIMARY KEY NOT NULL,
    cname TEXT NOT NULL,
    age INT NOT NULL,
    addr CHAR(50) ,
    salary REAL CHECK(salary>0),
    join_date DATE
);

CREATE TABLE IF NOT EXISTS Company_DB.com.Department (
    id INT PRIMARY KEY NOT NULL,
    dept CHAR(50) NOT NULL,
    emp_id  INT NOT NULL ,--REFERENCES(Company_DB.com.Company.id)   NOT NULL
);

-- use \d to list database
-- use \d tablename to get description on tablename
INSERT INTO Company_DB.com.Company (id,cname,age,addr,salary,join_date) VALUES (1, 'Google', 25, 'Mumbai', 20000.00,'2007-12-13');
INSERT INTO Company_DB.com.Company (id,cname,age,addr,salary,join_date) VALUES (2, 'Facebook', 25, 'Mumbai', 20000.00,'2007-12-13');
INSERT INTO Company_DB.com.Company (id,cname,age,addr,salary,join_date) VALUES (3, 'Microsoft', 22, 'Mumbai', 340000.00,'2007-12-13');
INSERT INTO Company_DB.com.Company (id,cname,age,addr,salary,join_date) VALUES (4, 'Apple', 34, 'Mumbai', 90000.00,'2007-12-13');
INSERT INTO Company_DB.com.Company (id,cname,age,addr,join_date) VALUES (5, 'Oracle', 89, 'Mumbai','2007-12-13');
INSERT INTO COMPANY (id,cname,age,addr,salary,join_date) VALUES (6, 'Mark', 78, 'Rich-Mond ', 65000.00, '2007-12-13' ), (7, 'David', 27, 'Texas', 85000.00, '2007-12-13');


INSERT INTO Company_DB.com.Department (id,dept,emp_id) VALUES (1, 'IT', 1),(2, 'HR', 2),(3, 'Sales', 3),(4, 'Marketing', 4),(5, 'Accounts', 5),(6, 'Finance', 6),(7, 'Sales', 7),(8, 'Marketing', 8),(9, 'Accounts', 9),(10, 'Finance', 10),(11, 'IT', 11),(12, 'HR', 12);
INSERT INTO Company_DB.com.Department (id,dept,emp_id) VALUES  (13, 'Sales', 13),(14, 'Marketing', 14),(15, 'Accounts', 15),(16, 'Finance', 16);
SELECT * FROM Company_DB.com.Company; --- this will list all the records in the table
SELECT (id,cname,age) FROM Company_DB.com.Company LIMIT 3; -- this will list the columns in the table
SELECT (id,cname,age) FROM Company_DB.com.Company LIMIT 3 OFFSET 2 ORDER BY age ASC; --- this will list the columns in the table

SELECT (id,cname,age) FROM Company_DB.com.Company LIMIT 3 OFFSET 2 ORDER BY age DESC;

SELECT (13+56)  AS ADDITION;

SELECT (id,cname) FROM Company_DB.com.Company WHERE id%2 == 0;

SELECT COUNT(*) AS "Record" FROM Company_DB.com.Company;

SELECT CURRENT_TIMESTAMP;

SELECT (id,cname,addr) FROM Company_DB.com.Company WHERE age >=20 AND salary >=60000.00; 

SELECT * FROM Company_DB.com.Company WHERE cname::text LIKE "%pp%" OR cname::text LIKE "_oo%";

SELECT * FROM Company_DB.com.Company WHERE age IN (30,60);

SELECT * FROM Company_DB.com.Company WHERE age NOT IN (30,60);

SELECT * FROM Company_DB.com.Company WHERE age BETWEEN 20 AND 40 ;

SELECT cname,sum(salary) AS "salary_by_asc" FROM  Company_DB.com.Company GROUP BY cname; 

UPDATE Company_DB.com.Company SET salary = salary + 10000.00 WHERE id = 2;
UPDATE Company_DB.com.Company SET addr = "New Dehli",salary += 1290.00 WHERE id = 3;

WITH CTE AS (SELECT (id,cname,age) FROM Company_DB.com.Company) SELECT * FROM CTE;

WITH moved_rows AS((DELETE FROM Company_DB.com.Company WHERE salary <=30000.00 RETURNING *));
INSERT INTO Company_DB.com.Company (SELECT * FROM moved_rows);--?? BUG
SELECT id,cname,age,addr,salary,join_date,dept FROM Company_DB.com.Company CROSS JOIN Company_DB.com.Department;
SELECT id,cname,age,addr,salary,join_date,dept FROM Company_DB.com.Company INNER JOIN Company_DB.com.Department ON Company_DB.com.Company.id = Company_DB.com.Company.id;


select w.channel as channel,w.occurred_at as time_at , a.primary_poc from web_events w join accounts a on w.account_id =a.id where a.name = 'Walmart';
select s.name rep , r.name region , a.name account from sales_reps s join region r on s.region_id = r.id 
join accounts a
on a.sales_rep_id= s.id 
order by a.name;


select r.name order_name , a.name account , (o.total_amt_usd/(o.total+0.01)) as unit 
from region r
join sales_reps s
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id;

select r.name region_name, s.name sales_rep_name
, a.name account_name 
from sales_reps s 
join region r
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
WHERE r.name = 'Midwest'
order by account_name;


select r.name region_name ,s.name sales_rep_name ,a.name account_name 
from sales_reps s
join region r
on s.region_id = r.id
join accounts a
on a.sales_rep_id  = s.id
where r.name  ='Midwest' and s.name like 'S%'
order by a.name;

select r.name region ,s.name sales_rep_name ,a.name account
from sales_reps s
join region r
on s.region_id = r.id
join accounts a
on a.sales_rep_id  = s.id
where r.name  ='Midwest' and s.name like '% K%'
order by a.name;


-- Provide the name for each region for every order, as well as the account name and 
-- the unit price they paid (total_amt_usd/total) for the order. 
-- However, you should only provide the results if the standard order quantity exceeds 100 and 
-- the poster order quantity exceeds 50. Your final table should have 3 columns: region name,
--  account name, and unit price.
--  Sort for the largest unit price first.


SELECT r.name region ,a.name account, (o.total_amt_usd/(o.total+0.01)) price
FROM orders o
JOIN accounts a 
ON a.id = o.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id
where o.standard_qty > and o.poster_qty > 50
ORDER BY price DESC;

select r.name region , a.name account, (o.total_amt_usd/(o.total+0.01)) price
from region r
join sales_reps s
on s.region_id = r.id
join accounts a
on a.sales_rep_id=s.id
join orders o
on a.id = o.account_id
where o.standard_qty > 100 and o.poster_qty >50
order by price;



SELECT DISTINCT
acc.name account , web.channel channel
FROM accounts acc
JOIN web_events web
ON web.account_id = acc.id
WHERE acc.id = '1001';

SELECT COUNT(orders.id)
FROM orders
WHERE orders.id IS  NULL;

select SUM(o.poster_qty) from orders o;
select SUM(o.standard_qty) from orders o;
select SUM(o.total_amt_usd) from orders o;
select SUM(o.total_amt_usd) + sUM(o.gloss_amt_usd) total_standard_gloss from orders o;
select MIN(o.occurred_at) from orders o;
select MAX(w.occurred_at) from web_events w;
select SUM(o.standard_amt_usd)/SUM(o.standard_qty) unit_per_paper from orders o;

SELECT occurred_at FROM orders ORDER BY occurred_at LIMIT 1;
SELECT occurred_at FROM web_events ORDER BY occurred_at DESC LIMIT 1;

SELECT AVG(standard_qty) mean_standard, AVG(gloss_qty) mean_gloss, 
           AVG(poster_qty) mean_poster, AVG(standard_amt_usd) mean_standard_usd, 
           AVG(gloss_amt_usd) mean_gloss_usd, AVG(poster_amt_usd) mean_poster_usd
FROM orders;
--- SELECT FROM <left_table> LEFT JOIN <right_table> ON <left_table>.<left_column> = <right_table>.<right_column>;
DELETE FROM Company_DB.com.Company WHERE id = 2;
-- DROP TABLE IF  EXISTS Company_DB.com.Department,Company_DB.com.Company;
-- DROP SCHEMA IF EXISTS Company_DB.com;

DROP SCHEMA IF EXISTS Company_DB.com CASCADE;
DROP DATABASE IF EXISTS Company_DB;
-- dropdb [options ....] dbname