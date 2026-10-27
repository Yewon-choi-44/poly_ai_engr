#수학 함수

select abs(-4.5);
select abs(-2.4); #절댓값

select ceil(4.1); #반올림
select floor(4.1); #반내림
select round(5.36, 1); #반올림, 자릿수
select log(10); #자연로그
select power(2,3); #n 제곱
select sqrt(9.0); # 제곱근
select sign(3.45); #음수면 -1, 0이면 0, 양수면 1

select round(115.36, -2);

select abs(-78), abs(78); #-78과 78의 절댓값
select round(4.875, 1); # 4.875를 소수 첫째 자리까지 반올림한 값
select custid '고객번호', round(sum(saleprice)/count(*),-1)'평균금액' from orders group by custid; 
select power(2,3), pow(10,2); #2의 3승과 10의2승
select mod(10,3), 10%3, mod(-10,3),mod(10,-3),mod(-10,-3); #10%3, -10%3, 10%-3,-10%-3
select floor(1+(rand()*10)), floor(rand()*100); #rand함수: 0이상 1미만 난수 생성, 괄호 안에 값 넣으면 랜덤시드 됨.

select truncate(123.4567, 2), truncate(123.4567,0), truncate(1234.4567,-2); #소수점 이하 숫자 잘라내기, -n 들어가면 정수부 n째 자리까지 자르고 나머지는 0으로 채움 



#문자 함수
select bookid, replace(bookname,'야구','농구') bookname,publisher, price from book; #replace():문자열 치환 함수 (바까서 출력하라고)

select trim('   공백   '); #양쪽 공백 제거
select trim('-'from'-----특정문자제거-----'); #특정문자 제거
select replace('------특정-문자----', '-', '');

select lpad(bookid, 4, '0') as padded_bookid, bookid from book; #문자열의 왼쪽자리부터 원하는 문자로 채워서 자릿수 맞춰주는 함수
select lpad(10, 4, '0');

select bookname '제목', char_length(bookname)'문자수', length(bookname)'바이트수' from book where publisher='굿스포츠'; #length() : 글자 수 세어주는 함수
select substr(name, 1, 1)'성',count(*)'인원' from customer group by substr(name, 1, 1); #substr(): 지정한 길이만큼의 문자열을 반환하는 함수
select substr(name, 2) '이름' from customer;
select substr(name, 1, 2) '이름' from customer; #substr(열, 시작, 어디까지 끊을건지)



#날짜/시간 함수
#show variables;

select orderid '주문번호', orderdate '주문일', adddate(orderdate, interval 10 day) '확정' from orders;
select orderid '주문번호', orderdate '주문일', adddate(orderdate, interval 60 day) '확정' from orders; #날짜를 더해서 디데이?계산?해줌

#select orderid '주문번호', str_to_date(orderdate, '%Y-%m-%d') '주문일', custid '고객번호', bookid '도서번호' from orders where orderdate = date_format('20230701', '%Y%m%d');
#select orderid '주문번호', str_to_date(orderdate, '%Y-%m-%d') '주문일', custid '고객번호', bookid '도서번호' from orders where orderdate = date_format('20230701', '%Y/%m/%d');
select orderid '주문번호', date_format(orderdate, '%Y-%m-%d') '주문일', custid '고객번호', bookid '도서번호' from orders where orderdate = str_to_date('20230701', '%Y%m%d');

select orderid'주문번호', STR_TO_DATE(orderdate,'%Y-%m-%d')'주문일', custid'고객번호',bookid'도서번호' from orders where orderdate=DATE_FORMAT('20230703','%Y%m%d');

desc orders; #orderdate의 데이터 type은 date< 이다. 
			 #비교할 때 str_to_date('20230701', '%Y%m%d')랑은 모양이 같은 거여야 한다. 자리 맞춰줘야 한다. 그래야 정상적으로 문자열이던 '20230701'에서 날짜 타입으로 데이터타입이 변경이 된다.
select * from orders;
select str_to_date('2023-0701', '%Y-%m%d');



select sysdate(), date_format(sysdate(), '%Y/%m/%d %M %h:%s') 'sysdate_1'; #sysdate : mysql의 현재 날짜, 시간 반환 함수
select null +100; 
select null + 10000000000000000000; #null < 비어있으면 멀 넣든 소용이 없셈
-- select 1000 + price from where price is not null; #이거는 에러뜰거임


select * from mybook where price is null; #null 찾을 땐  is null< 로 찾는다.
select * from exaggfn;
select * from exaggfn where col4 = null;
select * from exaggfn where col4 is null;
select * from exaggfn where col4 is not null;

select name '이름', '전화번호' from customer;
select name '이름', ifnull(phone, '연락처없음')'전화번호' from customer;
update customer set phone=null where custid=5;
select name, ifnull(phone, '없음') from customer;

set @seq:=0;
select (@seq:=@seq+1), '순번', custid, name, phone from customer;
# where @seq<2;



select orderid '주문번호', date_format(orderdate, '%Y-%m-%d') '주문일', custid '고객번호', bookid '도서번호' from orders where orderdate = str_to_date('20230701', '%Y%m%d');