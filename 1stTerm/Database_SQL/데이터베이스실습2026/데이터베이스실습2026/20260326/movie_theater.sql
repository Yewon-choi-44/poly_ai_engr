insert into movie (title, director, release_date) (select title, director, release_date FROM practice5.new_movie);
SET SQL_SAFE_UPDATES=0; 
delete from movie where release_date is null;
alter table movie modify release_date date not null;

CREATE TABLE Screen (
    id INTEGER PRIMARY KEY,
    theater_id INTEGER,
    name VARCHAR(40)
);
create table screenhist (
	id integer primary key auto_increment,
    screen_id integer not null,
    movie_id integer not null,
    reservation_cnt integer default 0,
    screening_date datetime not null,
    foreign key (screen_id) references screen (id),
    foreign key (movie_id) references movie(id));
select * from screen;


INSERT INTO screenhist (screen_id, movie_id, reservation_cnt, screening_date) (SELECT screen_id, movie_id, reservation_cnt, screening_date FROM practice5.screeninfo_05);
alter table screenhist add showtime_category varchar(10) default 'normal';
select * from screenhist;
set sql_safe_updates = 0;
UPDATE screenhist SET reservation_cnt = 10 WHERE screening_date >= '2024-05-01 00:00:00';
INSERT INTO screenhist (screen_id, movie_id, reservation_cnt, screening_date) (SELECT screen_id, movie_id, reservation_cnt, screening_date FROM practice5.screeninfo_05);

UPDATE screenhist SET showtime_category = 'early' WHERE DATE_FORMAT(screening_date, '%H:%i:%S') <= '10:00:00';

select t.name, s.name, m.title, sh.screening_date, sh.showtime_category 
from screenhist sh
join screen s ON sh.screen_id = s.id
join theater t ON s.theater_id = t.id
join movie m ON sh.movie_id = m.id
where DATE_FORMAT(sh.screening_date, '%m') = '05'
order by s.id, sh.screening_date;
 
select t.name, s.name, m.title, sh.screening_date, sh.showtime_category 
from screenhist sh
join screen s ON sh.screen_id = s.id
join theater t ON s.theater_id = t.id
join movie m ON sh.movie_id = m.id
order by s.id, sh.screening_date;

select * from screenhist as sh1 
where sh1.screening_date = 
(select min(screening_date) from screenhist
where DATE_FORMAT(screening_date, '%Y-%m-%d') = DATE_FORMAT(sh1.screening_date, '%Y-%m-%d')
	  and screen_id = sh1.screen_id
);

update screenhist set showtime_category = 'early1'  
where screening_date = 
(select min(sh2.screening_date) from screenhist as sh2
where DATE_FORMAT(sh2.screening_date, '%Y-%m-%d') = DATE_FORMAT(screening_date, '%Y-%m-%d')
)


update screenhist as sh1 set showtime_category = 'early1'  
where sh1.screening_date = 
(select min(sh2.screening_date) from screenhist as sh2
where DATE_FORMAT(sh2.screening_date, '%Y-%m-%d') = DATE_FORMAT(sh2.screening_date, '%Y-%m-%d')
	AND sh2.screen_id = sh1.screen_id
);

UPDATE screenhist AS sh1
SET sh1.showtime_category = 'early1'
WHERE sh1.screening_date = (
    SELECT MIN(sh2.screening_date)
    FROM screenhist AS sh2
    WHERE DATE_FORMAT(sh2.screening_date, '%Y-%m-%d') = DATE_FORMAT(sh1.screening_date, '%Y-%m-%d')
      AND sh2.screen_id = sh1.screen_id
);

UPDATE screenhist AS sh1
JOIN (
    SELECT sh2.screen_id, MIN(sh2.screening_date) AS min_screening_date
    FROM screenhist AS sh2
    GROUP BY sh2.screen_id, DATE(sh2.screening_date)
) AS min_screenings
ON sh1.screen_id = min_screenings.screen_id
   AND sh1.screening_date = min_screenings.min_screening_date
SET sh1.showtime_category = 'early1';