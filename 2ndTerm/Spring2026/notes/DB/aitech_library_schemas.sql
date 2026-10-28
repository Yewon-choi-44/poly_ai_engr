use aitech_library;
create database if not exists aitech_library
default character set utf8mb4
default collate utf8mb4_general_ci;



CREATE TABLE member(
	m_no int auto_increment primary key,
    m_id varchar(50) not null unique,
    m_pw varchar(100) not null,
    m_name varchar(50) not null,
    m_gender char(1),
    m_mail varchar(100),
    m_phone varchar(20),
    m_role varchar(10) not null default 'USER',
    m_reg_date datetime,
    m_mod_date datetime
);

create table book (
	b_no int auto_increment primary key,
    b_name varchar(200) not null,
    b_author varchar(200),
    b_publisher varchar(100),
    b_publish_year char(4),
    b_isbn varchar(20),
    b_call_number varchar(50),
    b_rental_able tinyint(1) not null default 1,
    b_img varchar(255),
    b_reg_date datetime,
    b_mod_date datetime
);

create table rentalbook (
	rb_no int auto_increment primary key,
    b_no int not null,
    m_no int not null,
    rb_start_date datetime not null,
    rb_end_date datetime null,
    rb_reg_date datetime,
    rb_mod_date datetime,
    foreign key (b_no) references book(b_no),
    foreign key (m_no) references member(m_no)
    
);
