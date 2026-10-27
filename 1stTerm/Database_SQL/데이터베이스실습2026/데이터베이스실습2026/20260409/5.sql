select * from customer;
select * from orders;
delete from customer where custid=3;

select custid, count(*)
from orders
where saleprice >= 8000
group by custid
having count(*) >= 2;
