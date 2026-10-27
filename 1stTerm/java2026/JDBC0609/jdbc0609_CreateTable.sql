-- 1.  여러 후보키 중 하나를 선정하여 대표로 삼은 키
-- 기본키

-- 2. 무결성 제약조건 3가지
-- 개체 무결성 제약조건, 참조 무결성 제약조건, 도메인 무결성 제약조건

-- 3. 데이터 정의어(DDL) 3가지 
-- ALTER, CREATE, DROP

-- 4. 데이터 조작어(DML) 4가지
-- INSERT, SELECT, UPDATE, DELETE

-- 5. 개체와 개체 간의 관계로 표현하는 모델
-- 관계 데이터 모델

-- 6. 
-- -- (1). 200행
-- -- (2). 200행
-- -- (3). 50행 

 -- 7. 개체 무결성 위반.
 
 -- 8. (1) (2) foreign (3) TEAM_ID (4) TEAM_ID2
 
 -- 9. Alpha
 
 -- 10. (1) 외래키 (2) 후보키 (3) 대체키 (4) 슈퍼키
 
 -- 11. 
 CREATE DATABASE foodcourt CHARSET UTF8MB4;
 
 -- 12.  
 CREATE TABLE restaurants(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    location VARCHAR(40) null,
    contact_number VARCHAR(40) null
    );

-- select * from restaurants ;


-- 13. 
CREATE TABLE menus(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INTEGER NOT NULL,
    item_name VARCHAR(40),
    price INTEGER NOT NULL,
    description VARCHAR(100) null,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
    );
select * from menus;
    
-- 14. 
CREATE TABLE orders(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    order_date datetime,
    total_amount INTEGER NOT NULL,
    customer_phone VARCHAR(20) null
    );

    
-- 15.
CREATE TABLE order_items(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    order_id INTEGER NOT NULL, 
    FOREIGN KEY(order_id) references orders(id),
    menu_id INTEGER NOT NULL,
    FOREIGN KEY(menu_id) references menus(id),
    order_number VARCHAR(20),
    quantity INTEGER DEFAULT 1,
    unit_price INTEGER DEFAULT 0
    );
    
-- 16.
INSERT INTO restaurants (name, location, contact_number) VALUES ("호우섬", "B1-001", "052-661-1234");
INSERT INTO restaurants (name, location, contact_number) VALUES ("홍대개미", "B1-002", "052-661-2134");
INSERT INTO restaurants (name, location, contact_number) VALUES ("페이페이", "B1-003", "052-661-1615");
INSERT INTO restaurants (name, location, contact_number) VALUES ("돈카츠렌", "B1-004", "052-661-1716");
INSERT INTO restaurants (name, location, contact_number) VALUES ("샤브진", "B1-005", "052-661-8111");
select * from restaurants;

-- 17.
-- INSERT INTO menus (restaurant_id, item_name, price, description)(SELECT restaurant_id, item_name, price, description FROM foodcourt.menus); 
INSERT INTO menus set restaurant_id = 1, item_name="마늘칩 꿔바육", price=22000, description="요리";
INSERT INTO menus set restaurant_id = 1, item_name="소롱포", price=7500, description="딤섬";
INSERT INTO menus set restaurant_id = 1, item_name="맑은 우육탕면", price=13000, description="누들";

INSERT INTO menus set restaurant_id = 2, item_name="스테이크 덮밥", price=11900, description="굽기조절불가";
INSERT INTO menus set restaurant_id = 2, item_name="큐브스테이크 덮밥", price=12900, description=" ";
INSERT INTO menus set restaurant_id = 2, item_name="연어 덮밥", price=15900, description=" ";

INSERT INTO menus set restaurant_id = 3, item_name="방콕 양지 쌍국수", price=10900, description="BEST";
INSERT INTO menus set restaurant_id = 3, item_name="하노이 소고기 쌀국수", price=9900, description=" ";
INSERT INTO menus set restaurant_id = 3, item_name="몽골리안 스테이크 덮밥", price=12900, description="BEST";
INSERT INTO menus set restaurant_id = 3, item_name="발리 나시고렝", price=9900, description=" ";

INSERT INTO menus set restaurant_id = 4, item_name="돈카츠렌 정식", price=16500, description="대표메뉴";
INSERT INTO menus set restaurant_id = 4, item_name="매운 왕 돈카츠", price=15500, description=" ";
INSERT INTO menus set restaurant_id = 4, item_name="카레 돈카츠", price=14500, description=" ";
INSERT INTO menus set restaurant_id = 4, item_name="로스 돈카츠", price=12500, description=" ";

INSERT INTO menus set restaurant_id = 5, item_name="소고기 야채 샤브샤브", price=15000, description=" ";
select * from menus;

-- 18.
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-1234-1234';
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-2001-1134';
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-1234-1234';
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-4573-1235';
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-2343-1343';
INSERT INTO orders set order_date = SYSDATE(), total_amount=0, customer_phone='010-1231-1112';
select * from orders;

-- 19.
-- INSERT--  INTO order_items (order_id, menu_id, order_number, quantity, unit_price)-- 





    
