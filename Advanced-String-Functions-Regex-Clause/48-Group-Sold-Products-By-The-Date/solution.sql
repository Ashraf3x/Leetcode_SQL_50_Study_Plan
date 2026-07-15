select 
    sell_date, 
    count(distinct product) as num_sold, 
    string_agg(product, ',') within group (order by product) as products
from (select distinct sell_date, product from activities) as t
group by sell_date
order by sell_date;