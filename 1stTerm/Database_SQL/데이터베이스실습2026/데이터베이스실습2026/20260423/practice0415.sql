DROP DATABASE IF EXISTS practice5;
CREATE database practice5 charset=utf8mb4;
USE practice5;

CREATE TABLE Book (
  bookid      INTEGER PRIMARY KEY,
  bookname    VARCHAR(40),
  publisher   VARCHAR(40),
  price       INTEGER 
);

CREATE TABLE  Customer (
  custid      INTEGER PRIMARY KEY,  
  name        VARCHAR(40),
  resident_number VARCHAR(24),
  address     VARCHAR(50),
  phone       VARCHAR(20)
);

CREATE TABLE Orders (
  orderid INTEGER PRIMARY KEY,
  custid  INTEGER ,
  bookid  INTEGER ,
  saleprice INTEGER ,
  orderdate DATE,
  FOREIGN KEY (custid) REFERENCES Customer(custid),
  FOREIGN KEY (bookid) REFERENCES Book(bookid)
);

INSERT INTO Book VALUES(1, '축구의 역사', '굿스포츠', 7000);
INSERT INTO Book VALUES(2, '축구아는 사람', '나무수', 13000);
INSERT INTO Book VALUES(3, '축구의 이해', '대한미디어', 22000);
INSERT INTO Book VALUES(4, '골프 바이블', '대한미디어', 35000);
INSERT INTO Book VALUES(5, '피겨 교본', '굿스포츠', 8000);
INSERT INTO Book VALUES(6, '역도 단계별기술', '굿스포츠', 6000);
INSERT INTO Book VALUES(7, '야구의 추억', '이상미디어', 20000);
INSERT INTO Book VALUES(8, '야구를 부탁해', '이상미디어', 13000);
INSERT INTO Book VALUES(9, '올림픽 이야기', '삼성당', 7500);
INSERT INTO Book VALUES(10, 'Olympic Champions', 'Pearson', 13000);

INSERT INTO Customer VALUES (1, '박지성', '810101-1111111', '영국 맨체스타', '000-5000-0001');
INSERT INTO Customer VALUES (2, '김연아', '900101-2222222', '대한민국 서울', '000-6000-0001');  
INSERT INTO Customer VALUES (3, '장미란', '830101-2333333', '대한민국 강원도', '000-7000-0001');
INSERT INTO Customer VALUES (4, '추신수', '820101-1444444', '미국 클리블랜드', '000-8000-0001');
INSERT INTO Customer VALUES (5, '박세리', '770101-2555555', '대한민국 대전',  NULL);

INSERT INTO Orders VALUES (1, 1, 1, 6000, STR_TO_DATE('2023-07-01','%Y-%m-%d')); 
INSERT INTO Orders VALUES (2, 1, 3, 21000, STR_TO_DATE('2023-07-03','%Y-%m-%d'));
INSERT INTO Orders VALUES (3, 2, 5, 8000, STR_TO_DATE('2023-07-03','%Y-%m-%d')); 
INSERT INTO Orders VALUES (4, 3, 6, 6000, STR_TO_DATE('2023-07-04','%Y-%m-%d')); 
INSERT INTO Orders VALUES (5, 4, 7, 20000, STR_TO_DATE('2023-07-05','%Y-%m-%d'));
INSERT INTO Orders VALUES (6, 1, 2, 12000, STR_TO_DATE('2023-07-07','%Y-%m-%d'));
INSERT INTO Orders VALUES (7, 4, 8, 13000, STR_TO_DATE( '2023-07-07','%Y-%m-%d'));
INSERT INTO Orders VALUES (8, 3, 10, 12000, STR_TO_DATE('2023-07-08','%Y-%m-%d')); 
INSERT INTO Orders VALUES (9, 2, 10, 7000, STR_TO_DATE('2023-07-09','%Y-%m-%d')); 
INSERT INTO Orders VALUES (10, 3, 8, 13000, STR_TO_DATE('2023-07-10','%Y-%m-%d'));

CREATE TABLE  Exaggfn (
  id      INTEGER PRIMARY KEY,  
  col1        VARCHAR(40),
  col2     	CHAR(50),
  col3        INTEGER,
  col4        INTEGER
);

INSERT INTO Exaggfn VALUES (1, 'col1', 'row1', 1, NULL);
INSERT INTO Exaggfn VALUES (2, 'col1', 'row2', 2, NULL);
INSERT INTO Exaggfn VALUES (3, 'col1', 'row3', 3, NULL);
INSERT INTO Exaggfn VALUES (4, 'col1', 'row4', NULL, NULL);
INSERT INTO Exaggfn VALUES (5, 'col1', NULL, 4, NULL);
INSERT INTO Exaggfn VALUES (6, 'col1', '', NULL, NULL);

-- 여기는 3장에서 사용되는 Imported_book 테이블
CREATE TABLE Imported_Book (
  bookid      INTEGER,
  bookname    VARCHAR(40),
  publisher   VARCHAR(40),
  price       INTEGER 
);

INSERT INTO Imported_Book VALUES(21, 'Zen Golf', 'Pearson', 12000);
INSERT INTO Imported_Book VALUES(22, 'Soccer Skills', 'Human Kinetics', 15000);

CREATE TABLE Mybook (
  bookid      INTEGER,
  price       INTEGER 
);

INSERT INTO Mybook VALUES(1, 10000);
INSERT INTO Mybook VALUES(2, 20000);
INSERT INTO Mybook VALUES(3, NULL);
commit;

CREATE TABLE Theater (
    id INTEGER PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(40),
    screen_count INTEGER,
    website VARCHAR(40)
);

INSERT INTO Theater VALUES(1, '롯데시네마 대구광장', '대구광역시 서구 달구벌대로 1691', 7, 'https://www.lottecinema.co.kr');
INSERT INTO Theater VALUES(2, 'CGV 대구죽전', '대구 달서구 달구벌대로 1551', 7, 'http://www.cgv.co.kr');
INSERT INTO Theater VALUES(3, '메가박스 프리미엄만경관', '대구 중구 국채보상로 547', 9, 'https://www.megabox.co.kr');
INSERT INTO Theater VALUES(4, 'CGV 대구현대', '대구광역시 중구 달구벌대로 2077', 6, 'http://www.cgv.co.kr');
INSERT INTO Theater VALUES(5, '메가박스 대구신세계', '대구 동구 동부로 149', 6, 'https://www.megabox.co.kr');


CREATE TABLE Screen (
    id INTEGER PRIMARY KEY,
    theater_id INTEGER,
    name VARCHAR(40)
);
INSERT INTO Screen VALUES(1, 1, '1관');
INSERT INTO Screen VALUES(2, 1, '2관');

INSERT INTO Screen VALUES(3, 2, '1관');
INSERT INTO Screen VALUES(4, 2, '2관');
INSERT INTO Screen VALUES(5, 2, '3관');
INSERT INTO Screen VALUES(6, 2, '6관');

INSERT INTO Screen VALUES(7, 3, '1관');
INSERT INTO Screen VALUES(8, 3, '2관');
INSERT INTO Screen VALUES(9, 3, '3관');

INSERT INTO Screen VALUES(10, 4, '1관');
INSERT INTO Screen VALUES(11, 4, '2관LASER');
INSERT INTO Screen VALUES(12, 4, '3관');
INSERT INTO Screen VALUES(13, 4, '4관LASER');
INSERT INTO Screen VALUES(14, 4, '5관');

INSERT INTO Screen VALUES(15, 5, '1관 Dolby Cinema');
INSERT INTO Screen VALUES(16, 5, '2관');
INSERT INTO Screen VALUES(17, 5, '3관');
INSERT INTO Screen VALUES(18, 5, '4관');

CREATE TABLE Movie (
    id INTEGER PRIMARY KEY,
    title VARCHAR(60),
    director VARCHAR(40),
    release_date DATE
);
INSERT INTO Movie VALUES(1, '파묘', '장재현', '2024-02-22');
INSERT INTO Movie VALUES(2, '듄:파트2', '드니빌뇌브', '2024-02-28');
INSERT INTO Movie VALUES(3, '남은 인생 10년', '후지이미치히토', '2024-04-01');
INSERT INTO Movie VALUES(4, '쿵푸팬더4', '마이크미첼', '2024-04-10');
INSERT INTO Movie VALUES(5, '고스트버스터즈:오싹한뉴욕', '길키넌', '2024-04-17');
INSERT INTO Movie VALUES(6, '범죄도시4', '허명행', '2024-04-24');
INSERT INTO Movie VALUES(7, '가디언즈 오브 갤럭시', '제임스건', '2024-05-03');
INSERT INTO Movie VALUES(8, '짱구는 못 말려:동물소환 닌자 배꼽수비대', '하시모토마사카즈', '2024-05-01');

CREATE TABLE new_screenhist (
    id INTEGER AUTO_INCREMENT,
    screen_id INTEGER,
    movie_id INTEGER,
    reservation_cnt INTEGER,
    screening_date DATETIME,
    PRIMARY KEY (id)
);

INSERT INTO new_screenhist VALUES(NULL, 1, 1, 100, '2024-04-19 16:40:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 1, 50, '2024-04-19 19:30:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 4, 30, '2024-04-19 15:20:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 4, 100, '2024-04-19 17:20:00');
INSERT INTO new_screenhist VALUES(NULL, 2, 4, 80, '2024-04-19 16:50:00');

-- CGV 대구죽전
INSERT INTO new_screenhist VALUES(NULL, 3, 4, 95, '2024-04-19 15:00:00');
INSERT INTO new_screenhist VALUES(NULL, 4, 5, 110, '2024-04-19 15:00:00');

-- CGV 대구현대
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 100, '2024-04-20 13:25:00');
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 181, '2024-04-20 17:00:00');
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 200, '2024-04-20 21:50:00');

-- 메가박스 대구 신세 
INSERT INTO new_screenhist VALUES(NULL, 15, 4, 141, '2024-04-21 16:40:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 4, 153, '2024-04-21 20:55:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 4, 151, '2024-04-21 22:55:00'); #13
INSERT INTO new_screenhist VALUES(NULL, 17, 4, 107, '2024-04-21 11:20:00');
INSERT INTO new_screenhist VALUES(NULL, 17, 4, 107, '2024-04-21 13:20:00');

INSERT INTO new_screenhist VALUES(NULL, 15, 6, 161, '2024-04-24 10:30:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 202, '2024-04-24 12:50:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 198, '2024-04-24 15:10:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 188, '2024-04-24 17:30:00');

INSERT INTO new_screenhist VALUES(NULL, 16, 6, 141, '2024-04-24 10:00:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 153, '2024-04-24 12:20:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 151, '2024-04-24 14:40:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 107, '2024-04-24 17:00:00');

CREATE TABLE new_movie (
    title VARCHAR(60),
    director VARCHAR(40),
    release_date DATE
);
INSERT INTO new_movie VALUES('혹성탈출:새로운시대', '웨스 볼', '2024-05-08');
INSERT INTO new_movie VALUES('인사이드아웃', '', '2024-06-08');
INSERT INTO new_movie VALUES('에이리언:로물루스', '페데 알바레즈', NULL);




CREATE TABLE new_screenhist (
    id INTEGER AUTO_INCREMENT,
    screen_id INTEGER,
    movie_id INTEGER,
    reservation_cnt INTEGER,
    screening_date DATETIME,
    PRIMARY KEY (id)
);

INSERT INTO new_screenhist VALUES(NULL, 1, 1, 100, '2024-04-19 16:40:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 1, 50, '2024-04-19 19:30:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 4, 30, '2024-04-19 15:20:00');
INSERT INTO new_screenhist VALUES(NULL, 1, 4, 100, '2024-04-19 17:20:00');
INSERT INTO new_screenhist VALUES(NULL, 2, 4, 80, '2024-04-19 16:50:00');

-- CGV 대구죽전
INSERT INTO new_screenhist VALUES(NULL, 3, 4, 95, '2024-04-19 15:00:00');
INSERT INTO new_screenhist VALUES(NULL, 4, 5, 110, '2024-04-19 15:00:00');

-- CGV 대구현대
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 100, '2024-04-20 13:25:00');
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 181, '2024-04-20 17:00:00');
INSERT INTO new_screenhist VALUES(NULL, 10, 2, 200, '2024-04-20 21:50:00');

-- 메가박스 대구 신세 
INSERT INTO new_screenhist VALUES(NULL, 15, 4, 141, '2024-04-21 16:40:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 4, 153, '2024-04-21 20:55:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 4, 151, '2024-04-21 22:55:00'); #13
INSERT INTO new_screenhist VALUES(NULL, 17, 4, 107, '2024-04-21 11:20:00');
INSERT INTO new_screenhist VALUES(NULL, 17, 4, 107, '2024-04-21 13:20:00');

INSERT INTO new_screenhist VALUES(NULL, 15, 6, 161, '2024-04-24 10:30:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 202, '2024-04-24 12:50:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 198, '2024-04-24 15:10:00');
INSERT INTO new_screenhist VALUES(NULL, 15, 6, 188, '2024-04-24 17:30:00');

INSERT INTO new_screenhist VALUES(NULL, 16, 6, 141, '2024-04-24 10:00:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 153, '2024-04-24 12:20:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 151, '2024-04-24 14:40:00');
INSERT INTO new_screenhist VALUES(NULL, 16, 6, 107, '2024-04-24 17:00:00');

CREATE TABLE screeninfo_05 (
    screen_id INTEGER,
    movie_id INTEGER,
    reservation_cnt INTEGER,
    screening_date DATETIME
);

INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 07:40:00');
INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 10:00:00');
INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 12:20:00');
INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 14:40:00');
INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 17:00:00');
INSERT INTO screeninfo_05 VALUES(16, 6, 0, '2024-05-01 19:00:00');
INSERT INTO screeninfo_05 VALUES(15, 6, 0, '2024-05-01 08:20:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 08:50:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 11:10:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 13:30:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 15:50:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 18:10:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 20:30:00');
INSERT INTO screeninfo_05 VALUES(14, 6, 0, '2024-05-01 22:50:00');
commit;