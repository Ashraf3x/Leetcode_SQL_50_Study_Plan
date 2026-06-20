select 
    round(avg(case when order_date = customer_pref_delivery_date then 100.0 else 0.0 end), 2) as immediate_percentage
from delivery d1
where order_date = (
    select min(order_date)
    from delivery d2
    where d1.customer_id = d2.customer_id
);