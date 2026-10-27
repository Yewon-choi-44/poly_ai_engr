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
commit;

CREATE TABLE Theater (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    theater_id INTEGER,
    name VARCHAR(40)
);
INSERT INTO Screen VALUES(1, 1, '4관');
INSERT INTO Screen VALUES(2, 1, '7관');

INSERT INTO Screen VALUES(3, 2, '1관');
INSERT INTO Screen VALUES(4, 2, '2관');
INSERT INTO Screen VALUES(5, 2, '3관');
INSERT INTO Screen VALUES(6, 2, '4DX관');

INSERT INTO Screen VALUES(7, 3, '컴포트1관');
INSERT INTO Screen VALUES(8, 3, '컴포트5관');

INSERT INTO Screen VALUES(9, 4, '1관');
INSERT INTO Screen VALUES(10, 4, '4관');

INSERT INTO Screen VALUES(11, 5, '2관');
INSERT INTO Screen VALUES(12, 5, '4관');
INSERT INTO Screen VALUES(13, 5, '5관');
INSERT INTO Screen VALUES(14, 5, '6관');


CREATE TABLE Movie (
    id INTEGER PRIMARY KEY,
    title VARCHAR(60),
    director VARCHAR(40),
    release_date DATE
);
INSERT INTO Movie VALUES(1, '프로젝트 헤일메리', '크리스토퍼 밀러', '2026-03-18');
INSERT INTO Movie VALUES(2, '왕과 사는 남자', '장항준', '2026-02-04');
INSERT INTO Movie VALUES(3, '네가 마지막으로 남긴 노래', '이키 타카히로', '2026-04-01');
INSERT INTO Movie VALUES(4, '귀멸의 칼날-무한성편', '소토자키 하루오', '2026-03-25');
INSERT INTO Movie VALUES(5, '펫 트레인', '쟝-크리스챤 태시', '2026-03-28');
INSERT INTO Movie VALUES(6, '끝장수사', '박철환', '2026-04-02');


CREATE TABLE screenhist (
    id INTEGER AUTO_INCREMENT,
    screen_id INTEGER,
    movie_id INTEGER,
    screening_date DATETIME,
    PRIMARY KEY (id)
);

INSERT INTO screenhist VALUES(NULL, 1, 1, '2026-04-01 11:35:00');
INSERT INTO screenhist VALUES(NULL, 1, 1, '2026-04-01 14:45:00');
INSERT INTO screenhist VALUES(NULL, 2, 1, '2026-04-01 10:40:00');
INSERT INTO screenhist VALUES(NULL, 2, 1, '2026-04-01 13:55:00');

-- CGV 대구죽전 
INSERT INTO screenhist VALUES(NULL, 3, 2, '2026-04-01 19:40:00');
INSERT INTO screenhist VALUES(NULL, 3, 2, '2026-04-01 22:05:00');
INSERT INTO screenhist VALUES(NULL, 3, 2, '2026-04-02 10:00:00');
INSERT INTO screenhist VALUES(NULL, 3, 2, '2026-04-02 12:25:00');

INSERT INTO screenhist VALUES(NULL, 4, 1, '2026-04-01 16:00:00');
INSERT INTO screenhist VALUES(NULL, 4, 1, '2026-04-01 19:05:00');

INSERT INTO screenhist VALUES(NULL, 5, 3, '2026-04-02 14:40:00');

INSERT INTO screenhist VALUES(NULL, 6, 4, '2026-04-03 13:00:00');
INSERT INTO screenhist VALUES(NULL, 6, 4, '2026-04-03 18:50:00');

-- 메가박스 프리미엄
INSERT INTO screenhist VALUES(NULL, 7, 1, '2026-04-02 09:40:00');
INSERT INTO screenhist VALUES(NULL, 8, 3, '2026-04-02 09:30:00');
INSERT INTO screenhist VALUES(NULL, 8, 3, '2026-04-02 11:40:00');


-- CGV 대구현대 
INSERT INTO screenhist VALUES(NULL, 9,  3, '2026-04-03 14:35:00');
INSERT INTO screenhist VALUES(NULL, 10, 5, '2026-03-31 10:40:00');


-- 메가박스 대구 신세 
INSERT INTO screenhist VALUES(NULL, 11, 6, '2026-04-03 20:50:00');
INSERT INTO screenhist VALUES(NULL, 12, 6, '2026-04-03 11:05:00');
INSERT INTO screenhist VALUES(NULL, 12, 2, '2026-04-03 15:40:00');
INSERT INTO screenhist VALUES(NULL, 13, 1, '2026-04-03 10:40:00');
INSERT INTO screenhist VALUES(NULL, 14, 2, '2026-04-03 10:30:00');

