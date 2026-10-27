create view vorders 
as select orderid, O.custid, name, O.bookid, bookname, saleprice, orderdate 
from customer C, Orders O, Book B 
where C.custid=O.custid and b.bookid = o.bookid;

select * from vorders;


# join을 써서도 voreders_2를 만들어라.
create view voreders_2
as select orderid, o.custid, name, o.bookid, bookname, saleprice, orderdate
from customer c join orders o on c.custid=o.custid join book;
show create view voreders_2;
##############################################################
# 뷰의 생성
# 실에 sql 문에서 테이블과 동일하게 사용할 수 있는 데이터베이스 개체
# 뷰의 정의를 뷰의 생성이라고도 함
# 뷰를 생성하는 문법
# create view 뷰이름 [(열이름 [ ,...,n])] as select문
# book 테이블에서 '축구'라는 문구가 포함된 자료만 보여주는 뷰를 만들어보기
# 뷰에 사용할 select문
select * from book where bookname like '%축구%';
# 위 select문을 이용해 뷰 정의문을 작성하면 당므과 같음
create view vw_Book as select * from book where bookname like '%축구%';
###############################################################
# 질의 4-10
# 주소에 '대한민국'을 포함하는 고객들로 구성된 뷰를 만들고 조회하시오. 뷰의 이름은 vw_Customer로 설정하시오.
create view vw_customer as select * from customer where address like '%대한민국%';
select * from vw_Customer;

select * from vorders where name = '김연아';
select * from vorders where name = '박지성';

###################################################################
# 뷰를 수정하는 문장
# create view문에 or replace 명령을 더하여 작성
# create or replace view 뷰이름 [(열이름 [,...n])] as select문
create or replace view  vw_customer(custid, name, address)
as select custid, name, address from customer where address like '%영국%';

select * from vw_customer;
##################################################################
# 뷸르 삭제하는 문장
# 뷰가 필요 없어졌다면 drop문을 사용하여 뷰를 삭제함
# drop view 뷰이름 [,...n];

#질의 4-23. 앞서 생성한 뷰 vw_customer를 삭제하시오.
drop view vw_customer;
select * from vw_customer;
# show views; <= 이런 명령어는 없음
# show tables; <= 이건 또 있음

######################################################
#인덱스의 생성
#질의 4-24. book 테이블의 bookname 열을 대상으로 인덱스 ix_book을 생성하시오.
create index ix_book on book(bookname);

#질의 4-25. book 테이블의 publisher, price 열을 대상으로 인덱스 ix_book2를 생성하시오.
create index ix_book2 on book(publisher, price);
explain select * from book where publisher ='대한미디어' and price >= 30000;
explain select * from book where bookname = '야구를 부탁해';
explain select * from book where publisher = '대한미디어';


drop index ix_book on book;
show indexes from book;
