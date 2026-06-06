select product_name , year , price
from Product join Sales
on Product.product_id  = Sales.product_id   
