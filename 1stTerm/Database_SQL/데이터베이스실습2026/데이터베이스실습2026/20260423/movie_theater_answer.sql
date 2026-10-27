create database movie_theater charset utf8mb4;
CREATE TABLE theater (
    id             INTEGER PRIMARY KEY AUTO_INCREMENT,
    name           VARCHAR(40) NOT NULL,
    address        VARCHAR(100),
    screen_cnt     INTEGER,
    website        VARCHAR(50)
);
CREATE TABLE screen (
    id          INTEGER PRIMARY KEY AUTO_INCREMENT,
    theater_id  INTEGER NOT NULL,
    name        VARCHAR(40),
    FOREIGN KEY (theater_id) REFERENCES theater (id)
);
CREATE TABLE movie (
    id            INTEGER PRIMARY KEY AUTO_INCREMENT,
    title         VARCHAR(15) NOT NULL,
    director      VARCHAR(50),
    release_date  DATE NOT NULL
);
CREATE TABLE screenhist (
    id               INTEGER PRIMARY KEY AUTO_INCREMENT,
    screen_id        INTEGER NOT NULL,
    movie_id         INTEGER NOT NULL,
    reservation_cnt  INTEGER DEFAULT 0, #값을 입력하지 않으면 기본값 0가 된다.
    screening_date   DATETIME NOT NULL,
    FOREIGN KEY (screen_id) REFERENCES screen (id),
    FOREIGN KEY (movie_id) REFERENCES movie (id)
);

INSERT INTO Theater VALUES(1, '롯데시네마 대구광장', '대구광역시 서구 달구벌대로 1691', 7, 'https://www.lottecinema.co.kr');
INSERT INTO Theater VALUES(2, 'CGV 대구죽전', '대구 달서구 달구벌대로 1551', 7, 'http://www.cgv.co.kr');
INSERT INTO Theater VALUES(3, '메가박스 프리미엄만경관', '대구 중구 국채보상로 547', 9, 'https://www.megabox.co.kr');
INSERT INTO Theater VALUES(4, 'CGV 대구현대', '대구광역시 중구 달구벌대로 2077', 6, 'http://www.cgv.co.kr');
INSERT INTO Theater VALUES(5, '메가박스 대구신세계', '대구 동구 동부로 149', 6, 'https://www.megabox.co.kr');

INSERT  INTO screen SELECT * FROM  practice5.screen;

select * from screen;

INSERT INTO Theater VALUES(6, 'CGV 대구한일', '대구 중구 동성로 39', 5, 'https://www.cgv.co.kr');

INSERT INTO Screen VALUES(19, 6, '씨네앤포레관');
INSERT INTO Screen VALUES(20, 6, '3관');

-- 오류 발생
UPDATE theater SET id = 10 WHERE name = 'CGV 대구한일';

ALTER TABLE screen DROP FOREIGN KEY screen_ibfk_1;

alter table screen ADD FOREIGN KEY (theater_id) REFERENCES theater(id) ON UPDATE CASCADE;

UPDATE theater SET id = 10 WHERE name = 'CGV 대구한일';
set sql_safe_updates=0;

select * from screen;

delete from theater where name = 'CGV 대구한일';

show create table screen;

ALTER TABLE screen DROP FOREIGN KEY screen_ibfk_1;

ALTER TABLE screen ADD FOREIGN KEY (theater_id) REFERENCES theater(id) ON DELETE CASCADE ON UPDATE CASCADE;

INSERT INTO Movie VALUES(1, '파묘', '장재현', '2024-02-22');
INSERT INTO Movie VALUES(2, '듄:파트2', '드니빌뇌브', '2024-02-28');
INSERT INTO Movie VALUES(3, '남은 인생 10년', '후지이미치히토', '2024-04-01');
INSERT INTO Movie VALUES(4, '쿵푸팬더4', '마이크미첼', '2024-04-10');
INSERT INTO Movie VALUES(5, '고스트버스터즈:오싹한뉴욕', '길키넌', '2024-04-17');
INSERT INTO Movie VALUES(6, '범죄도시4', '허명행', '2024-04-24');
INSERT INTO Movie VALUES(7, '가디언즈 오브 갤럭시', '제임스건', '2024-05-03');
INSERT INTO Movie (id, title, director, release_date) VALUES(8, '짱구는 못 말려:동물소환 닌자 배꼽수비대', '하시모토마사카즈', '2024-05-01');

alter table movie modify title varchar(100);
alter table movie modify release_date date null;

INSERT INTO movie (title, director, release_date) (SELECT title, director, release_date FROM practice5.new_movie);

select * from movie;

ALTER TABLE movie ADD running_time INTEGER DEFAULT 0;

ALTER TABLE movie change running_time play_time INTEGER DEFAULT 0;

INSERT INTO screenhist (screen_id, movie_id, reservation_cnt, screening_date) (SELECT screen_id, movie_id, reservation_cnt, screening_date FROM practice5.new_screenhist);
select * from screenhist;

INSERT INTO screenhist (screen_id, movie_id, reservation_cnt, screening_date) (SELECT screen_id, movie_id, reservation_cnt, screening_date FROM practice5.screeninfo_05);

alter table screenhist add showtime_category varchar(10);

UPDATE screenhist SET reservation_cnt = 10 WHERE screening_date >= '2024-05-01 00:00:00';

SELECT DATE_FORMAT(screening_date, '%H:%i:%S') AS TIME FROM screenhist;

