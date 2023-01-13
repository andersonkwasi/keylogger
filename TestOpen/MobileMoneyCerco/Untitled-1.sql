create function FindAverageCost(sellDate varchar(10)) 
returns INT DETERMINISTIC 
RETURN (select avg(Cost) 
from Orders
where Orders.Date = sellDate)
