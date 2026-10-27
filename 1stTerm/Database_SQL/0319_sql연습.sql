select *, bookname as bname from Book order by bookname;
select bookname as bname,b.* from Book as b order by bookname;
select * from Book order by price, bookname;
select * from Book order by price DESC, publisher ASC;

#1. 박지성 고객(customer)의 전화번호(phone)을 찾으시오.
select phone from customer where name = "박지성";

#2. 도서(book) 피격 교본의 출판사(publisher)를 찾으시오.
select publisher from book where bookname="피겨%교본";

#3. 가격(price)이 8000원 이상인 도서(book)를 찾으시오.
select * from book where price >= 8000;

#4. 가격이 8000원 이상 15000원 이하인 도서(book)를 찾으시오.
select* from Book where price between 8000 and 15000;
select* from Book where price >= 8000 and price <= 15000;

#5. 도서(book) 이름에 '역사'가 포함된 도서를 찾으시오.
select * from book where bookname like "%역사%";

#6. 도서(book) 이름에 왼쪽 3번째 위치에 '의'라는 문자열을 같은 도서를 찾으시오.
select * from book where bookname like "%__의%";

#집계함수
select sum(saleprice) as "총매출" from orders where custid=2;
select sum(saleprice) as Total, avg(saleprice) as Average, min(saleprice) as Minimum, max(saleprice) as Maximum from orders;

select count(*) from orders;
select custid from customer where name="박지성";

#박지성의 주문한 횟수 찾기
select custid from customer where name="박지성";
select count(*) from orders where custid=1;

select * from customer;
select count(distinct custid) from orders;
select count(*) from orders;
select * from orders order by saleprice;

select custid,
 count(*) as "도서수량", sum(saleprice) as 총액 from orders group by custid;

