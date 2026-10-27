select bookname from book where price = (select max(price) from book);

#질의 3-29 도서를 구매한 적이 있는 고객의 이름을 검색하시오.
select name from customer where custid in (select custid from orders);

#질의 3-30 대한미디어에서 출판한 도서를 구매한 고객의 이름을 보이시오.]
select name from customer where custid in (select custid from orders where bookid in (select bookid from book where publisher="대한미디어"));
select name from customer c join orders o on c.custid = o.custid join book b on o.bookid=b.bookid where b.publisher = "대한미디어";

#질의 3-31 출판사별로 출판사의 평균 도서 가격보다 비싼 도서를 구하시오.
select b1.bookname from book b1 where b1.price>(select avg(b2.price) from book b2 where b2.publisher = b1.publisher);

#질의 3-32 대한민국에서 거주하는 고객의 이름과 도서를 주문한 고객의 이름을 보이시오.
select name from customer where address like "대한민국%" union select name from customer where custid in (select custid from orders);

#대한민국에서 거주한느 고객의 이름에서 도서를 주문한 고객의 이름 빼고 보이시오.(차집합)
select name from customer where address like "대한민국%" and name not in (select name from customer where custid in (select custid from orders));
#except(select name from customer where custid in (select custid from orders));


#대한민국에서 거주하는 고객 중 도서를 주문한 고객의 이름을 보이시오.(교집합)
select name from customer where address like "대한민국%" and name in (select name from customer where custid in (select custid from orders));
#intersect(select name from customer where custid in (select custid from orders));


create database practice3 charset utf8mb4;
drop database practice3;

show databases;

use practice3;

create table	NewBook_(
bookid 		integer, 
bookname	 varchar(20), 
publisher 	varchar(20), 
price	 integer,
primary key 	(bookname, publisher, price));

show create table newbook_;


create table neworders(
orderid integer, custid integer not null, bookid integer not null, saleprice integer, orderdate date, 

show create

#newbook에 saleprice(int)를 추가하세요.
