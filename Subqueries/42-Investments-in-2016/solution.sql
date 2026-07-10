with cte as (
    select tiv_2016,
           count(*) over(partition by tiv_2015) as tiv_cnt,
           count(*) over(partition by lat, lon) as loc_cnt
    from insurance
)
select round(sum(tiv_2016), 2) as tiv_2016
from cte
where tiv_cnt > 1 and loc_cnt = 1