select product_id, year as first_year, quantity, price 
from sales s
where year = (select  min(year) from  sales where product_id = s.product_id);