CREATE DATABASE FOODCOURT2 CHARSET UTF8MB4;
CREATE TABLE RESTAURANTS (
	ID INTEGER AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(40),
    LOCATION VARCHAR(40) NULL,
    CONTACT_NUMBER VARCHAR(40) NULL
    );
    
create table menus ( 
id integer auto_increment primary key, 
restaurant_id integer, 
item_name varchar(40), 
price integer default 0, 
description varchar(100) null, 
foreign key (restaurant_id) references restaurants(id) ); 

create table orders ( 
id integer auto_increment primary key, 
order_date datetime, 
total_amount integer default 0, 
customer_phone varchar(20) null );

create table order_items ( 
     id integer auto_increment primary key, 
     order_id integer, 
     menu_id integer, 
     order_number varchar(20), 
     quantity integer default 1, 
     unit_price integer default 0, 
     foreign key (order_id) references orders(id), 
     foreign key (menu_id) references menus(id) );
     
insert into restaurants(id,name,location,contact_number) values(1,"호우섬","B1-001","053-661-1234"); 
insert into restaurants(id,name,location,contact_number) values(2,"홍대개미","B1-002","053-661-2134"); 
insert into restaurants(id,name,location,contact_number) values(3,"페이페이","B1-003","053-661-1615"); 
insert into restaurants(id,name,location,contact_number) values(4,"돈카츠렌","B1-004","053-661-1716"); 
insert into restaurants(id,name,location,contact_number) values(5,"샤브진","B1-005","053-661-8111");

insert into menus(id,restaurant_id,item_name,price,description) values(1,1,"마늘칩 꿔바육",22000,"요리"); 
insert into menus(id,restaurant_id,item_name,price,description) values(2,1,"소롱포",7500,"딤섬"); 
insert into menus(id,restaurant_id,item_name,price,description) values(3,1,"맑은 우육탕면",13000,"누들"); 
insert into menus(id,restaurant_id,item_name,price,description) values(4,2,"스테이크 덮밥",11900,"굽기조절불가"); 
insert into menus(id,restaurant_id,item_name,price) values(5,2,"큐브스테이크 덮밥",12900); 
insert into menus(id,restaurant_id,item_name,price) values(6,2,"연어 덮밥",15900); 
insert into menus(id,restaurant_id,item_name,price,description) values(7,3,"방콕 양지 쌀국수",10900,"BEST"); 
insert into menus(id,restaurant_id,item_name,price) values(8,3,"하노이 소고기 쌀국수",9900); 
insert into menus values(9,3,"몽골리안 스테이크 덮밥",12900,"BEST"); 
insert into menus(id,restaurant_id,item_name,price) values(10,3,"발리 나시고렝",9900); 
insert into menus(id,restaurant_id,item_name,price,description) values(11,4,"돈카츠렌 정식",16500,"대표메뉴"); 
insert into menus(id,restaurant_id,item_name,price) values(12,4,"매운 왕 돈카츠",15500); 
insert into menus(id,restaurant_id,item_name,price) values(13,4,"카레 돈카츠",14500); 
insert into menus(id,restaurant_id,item_name,price) values(14,4,"로스 카츠",12500); 
insert into menus values(15,5,"소고기 야채 샤브샤브",15000,"단일메뉴");

insert into orders(id,order_date,customer_phone) values(1,'2026-06-17 12:30:00', ‘010-1234-1234’); 
insert into orders values(2, '2026-06-17 12:40:00', 0 , '010-2001-1134'); 
insert into orders(id,order_date,customer_phone) values(3,STR_TO_DATE('2026-06-17 12:51:00','%Y-%m-%d %H:%i:%s'),"010-1234-1234"); 
insert into orders values(4,STR_TO_DATE('2026-06-17 13:00:00','%Y-%m-%d %H:%i:%s'),"010-4573-1235"); 
insert into orders values(5, '2026-06-17 13:20:00',0, '010-2343-1343'); 
insert into orders values(6, '2026-06-17 13:35:00',0, "010-1231-1112");

insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(1,1,1,"1001",1,22000); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(2,1,2,"1002",2,15000); 
insert into order_items values(1,3,"1003",1,13000); 
insert into order_items values(NULL,2,(SELECT id FROM menus WHERE item_name='스테이크 덮밥'),"2001",1,11900); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(5,2,6,"2002",1,15900); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(6,3,7,"3001",2,10900); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(7,4,15,"5001",2,15000); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(8,5,5,"2003",1,12900); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(9,5,10,"3002",1,9900); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(10,5,11,"4001",1,16500); 
insert into order_items(id,order_id,menu_id,order_number,quantity,unit_price) values(11,6,13,"4002",1,14500); 