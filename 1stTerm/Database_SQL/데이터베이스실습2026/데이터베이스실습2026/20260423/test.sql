SELECT T.name, S.name, M.title, SH.screening_date
FROM ScreenHist AS SH 
     JOIN Screen AS S ON SH.screen_id = S.id 
     JOIN Theater AS T ON S.theater_id = T.id
     JOIN movie AS M ON SH.movie_id = M.id
WHERE  T.name = '메가박스 대구신세계' 
           AND screening_date >= '2024-04-21 00:00:00' 
           AND screening_date < '2024-04-22 00:00:00';

select * from movie;

desc movie;

set foreign_key_checks=0;
drop table movie;

CREATE TABLE movie (
    id            INTEGER PRIMARY KEY AUTO_INCREMENT,
    title         VARCHAR(30) NOT NULL,
    director      VARCHAR(50),
    release_date  DATE NOT NULL
);


alter table movie modify title varchar(30) not null;
select char_length('짱구는 못 말려:동물소환 닌자 배꼽수비대~~~~~~~~~~~~~~~~~~~~~~');
select @@sql_mode;

insert into movie set title="짱구는 못 말려:동물소환 닌자 배꼽수비대~~~~~~~~~~~~~~~~", director="------------", release_date='2023-04-15';

show create table movie;

select * from movie;

delete from movie where id=14;