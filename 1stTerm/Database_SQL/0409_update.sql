select * from customer;
#insert into customer values(5 , '박세리' , '대한민국대전' , '000-000-000');
update customer set address='대한민국 부산' where custid=5;
update customer set phone = '010-1234-1234' where custid=5;

set sql_safe_updates=0;
update customer set phone = '010-1234-1234';
update book set publisher = (select publisher from imported_book where bookid ='21') where bookid = '14';
update book set publisher = 'Pearson' where bookid=14;

select * from imported_book;
-- select publisger from imported

set sql_safe_updates=0; 
update customer set address='대한민국 부산' where custid=5;

-- 실행안된느 구문-- 
--  set sql_safe_updates=1;
-- update customer set address='대한민국 부산' where address like '대한%' update customer set address='대한민국 대구'


update customer set address = '대한민국 대구' where address like '대한%';
-- 영국으로 시작하는 주소를 가지는 사람의 주소를 대한민국 서울로 변경
update customer set address = '대한민구 서울' where address like '영국%';

delete from book where bookid=18;
delete from customer; #일부만 지울 때는 이거 씀 / dml에 속한다...

select * from customer;
truncate customer; #전부 다 지울 때는 이거 씀 / ddl에 속한다...

show databases;

use information_schema;
show tables;
-- select * from TABLE_CONSTRAINTS where table_name='neworders';

select * from orders;
select * from orders limit 2,10;


