select 
    m.employee_id, 
    m.name, 
    count(e.employee_id) as reports_count, 
    cast(round(avg(e.age * 1.0), 0) as int) as average_age
from employees m
join employees e 
    on m.employee_id = e.reports_to
group by 
    m.employee_id, 
    m.name
order by 
    m.employee_id;