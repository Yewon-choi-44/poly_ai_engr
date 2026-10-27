select * from book order by price, bookname desc;

select phone from customer where name = '박지성';
select publisher, bookname from book where bookname like '피겨%교본';
select * from book where price >= 8000;

select * from book where price between 8000 and 15000;
select * from book where bookname like '%역사%';
select * from book where bookname like '__의%';
select * from orders;

select sum(saleprice) sum from orders where custid=2;
select * from orders where custid=2;

select * from customer;

select sum(saleprice) t, avg(saleprice) a, 
min(saleprice) min, max(saleprice) max 
from orders;

select count(*) from orders where custid=1;
select * from orders where custid=1;

select * from customer;
select count(distinct custid) from orders;
select count(*) from orders;
select * from orders order by saleprice;

select bookid, count(*) as 도서별판매횟수 
from orders group by bookid;