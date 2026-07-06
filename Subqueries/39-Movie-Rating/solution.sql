select results 
from (
    select top 1 u.name as results
    from users u
    join movierating mr on u.user_id = mr.user_id
    group by u.user_id, u.name
    order by count(*) desc, u.name asc
) a
union all
select results 
from (
    select top 1 m.title as results
    from movies m
    join movierating mr on m.movie_id = mr.movie_id
    where mr.created_at >= '2020-02-01' and mr.created_at <= '2020-02-29'
    group by m.movie_id, m.title
    order by avg(cast(mr.rating as float)) desc, m.title asc
) b