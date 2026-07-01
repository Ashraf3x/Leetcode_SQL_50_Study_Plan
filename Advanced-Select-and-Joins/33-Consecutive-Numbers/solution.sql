select distinct num as consecutivenums
from (
    select num,
           lag(num, 1) over(order by id) as num1,
           lag(num, 2) over(order by id) as num2
    from logs
) as t
where num = num1 and num = num2