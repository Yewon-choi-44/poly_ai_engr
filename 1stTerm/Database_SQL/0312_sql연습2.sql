select bookname, price from book;
select price, bookname from book;

select bookname,publisher from book where bookname LIKE '%축구%';
#야
-- 이봐
/*어이*/
select * from book where publisher in ('굿스포츠','대한미디어');
select * from book where publisher=('굿스포츠') or publisher=('대한미디어');
select * from book where publisher != '굿스포츠' and publisher <> '대한미디어'; #중요
select bookname, publisher from book where bookname like '축구의 역사';
select bookname, publisher from book where bookname like '%축구%';
select * from book where bookname like '_구%';

#도서이름의 왼쪽 3번째 위치에 '의'라는 문자열을 갖는 도서를 검색하시오.
select * from book where bookname like '__의%';

select * from book where bookname like '%이%';
select * from book where bookname like '%축구%' and price >= 20000;
select * from book where bookname like '%야구%' and price < 20000;
select * from book where publisher = '굿스포츠' or publisher = '대한미디어';