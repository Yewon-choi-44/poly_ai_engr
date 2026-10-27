create user madang@localhost identified by 'madang';
grant all privileges on bookstore.*TO madang@localhost;
commit; flush privileges;
use mysql;
