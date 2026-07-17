select user_id, name, mail
from Users
where mail like '[a-z]%@leetcode.com' 
and mail not like '%[^a-z0-9_.-]%@leetcode.com'