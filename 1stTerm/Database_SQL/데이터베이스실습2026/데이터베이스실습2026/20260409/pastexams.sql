
drop database if exists pastexams;

create database pastexams charset=utf8mb4;

use pastexams;

create table salary (
	empno int,
    sal int
);

insert into salary values (100, 1000);
insert into salary values (200, 3000);
insert into salary values (300, 1500);

select count(*) from salary where empno > 100 and sal >= 1500 or empno >= 200 and sal >= 1000;

create table emp (
	id int,
    name varchar(20)
);

insert into emp values (1001, '김철수');
insert into emp values (1002, '홍길동');
insert into emp values (1004, '강감찬');
insert into emp values (1008, '이순신');

create table sal (
	id int,
    incentives int
);

insert into sal values (1002, 300);
insert into sal values (1004, 300);
insert into sal values (1008, 1000);
insert into sal values (1009, 500);

select name, incentives from emp, sal where emp.id = sal.id and incentives >= 500;


create table employee (
	no int,
    first_name varchar(20),
    last_name varchar(20),
    project_id int);

insert into employee values (1, 'John', 'Doe', 10);
insert into employee values (1, 'Jim', 'Carry', 20);
insert into employee values (1, 'Rachel', 'Redmond', 10);

create table project (
	project_id int,
    name varchar(20));

insert into project values(10, 'Alpha');
insert into project values(20, 'Beta');
insert into project values(10, 'Gamma');

select count(*) from employee as e join project as p on e.project_id = p.project_id 
where p.name in (select name from project p where p.project_id in (
	select project_id from employee group by project_id having count(*) < 2));
    

create table A (
	col1 int null,
    col2 int null
);

insert into A values(2, null);
insert into A values(3, 6);
insert into A values(2, 3);
insert into A values(null, 3);
insert into A values(4, 5);

SELECT count(col2) FROM A WHERE col1 IN (2, 3) OR col2 IN (3, 5);


create table monthly_sales (
	년 char(4),
    월 char(2),
    매출금액 int,
    primary key(년, 월)
);

insert into monthly_sales values('2014', '01', 1000);
insert into monthly_sales values('2014', '02', 2000);
insert into monthly_sales values('2014', '03', 3000);
insert into monthly_sales values('2014', '11', 4000);
insert into monthly_sales values('2014', '12', 5000);
insert into monthly_sales values('2015', '01', 6000);
insert into monthly_sales values('2015', '02', 7000);
insert into monthly_sales values('2015', '03', 8000);
insert into monthly_sales values('2015', '11', 9000);
insert into monthly_sales values('2015', '12', 10000);

select * from monthly_sales;
SELECT SUM(매출금액) AS 매출금액합계 FROM monthly_sales 
WHERE 년 = '2014' AND 월 BETWEEN '11' AND '12' 
   OR 년 = '2015' AND 월 BETWEEN '01' AND '03';
