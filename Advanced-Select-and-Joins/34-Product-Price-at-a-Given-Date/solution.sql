select product_id, new_price as price
from (
    select product_id, new_price, 
           row_number() over(partition by product_id order by change_date desc) as rn
    from products
    where change_date <= '2019-08-16'
) as t
where rn = 1
union
select distinct product_id, 10 as price
from products
where product_id not in (
    select product_id
    from products
    where change_date <= '2019-08-16'
)