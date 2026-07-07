with daily_sales as (
    select visited_on, sum(amount) as daily_total
    from customer
    group by visited_on
),
moving_stats as (
    select 
        visited_on,
        sum(daily_total) over(order by visited_on rows between 6 preceding and current row) as amount,
        round(sum(daily_total) over(order by visited_on rows between 6 preceding and current row) / 7.0, 2) as average_amount,
        row_number() over(order by visited_on) as day_num
    from daily_sales
)
select visited_on, amount, average_amount
from moving_stats
where day_num >= 7
order by visited_on