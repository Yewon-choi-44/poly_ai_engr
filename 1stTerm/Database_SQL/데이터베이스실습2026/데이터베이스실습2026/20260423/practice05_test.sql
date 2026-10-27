SELECT  POWER(2, 3), POW(10, 2);

SELECT MOD(10, 3), 10 % 3, MOD(-10, 3), MOD(10, -3), MOD(-10, -3);

select -10 - 3 * FLOOR(-10 / 3);

SELECT FLOOR(1 + (RAND() * 10)), FLOOR(RAND() * 100);

SELECT  TRUNCATE(123.4567, 2), TRUNCATE(123.4567, 0), TRUNCATE(1234.4567, -2);

desc orders;

select * from orders;

SELECT	orderid '주문번호', STR_TO_DATE(orderdate, '%Y-%m-%d') '주문일', 
               custid '고객번호', bookid '도서번호'
FROM	Orders
WHERE      orderdate= DATE_FORMAT('20230703', '%Y%m%d');

select * from mybook where price = NULL;

desc orders;

alter table orders add bookname varchar(40);
select c.name, od.custid, sum(saleprice) from orders od join customer c on c.custid = od.custid group by od.custid;
