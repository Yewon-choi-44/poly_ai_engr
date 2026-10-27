/*use madang;
select bookname, publisher from book;
select bookname, publisher from book where price >=10000;
desc book;*/

SELECT DISTINcT publisher from book;
select * from bOok where price<20000;
select * from book where price between  10000 and 20000;
select * from book where price >=10000 and price <=20000;
select * from book order by bookname;
select * from book order by price;
select * from book order by price desc;
select * from book order by price,bookname;
select * from book order by price desc, bookname;
select * from book order by price desc,bookname desc;
select * from book order by price desc, publisher asc;
