select name , bonus       
from Employee left join Bonus
on Employee.empId = Bonus.empId
where Bonus < 1000 or Bonus is null;