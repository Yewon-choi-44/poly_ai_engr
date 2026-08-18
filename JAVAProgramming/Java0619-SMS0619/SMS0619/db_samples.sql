create database smsdb;
USE smsdb;

CREATE TABLE departments (
    dept_code VARCHAR(10) NOT NULL,          -- 학과 고유 코드 (예: 'CS', 'EE')
    dept_name VARCHAR(50) NOT NULL,          -- 학과명 (예: '컴퓨터공학과')
    PRIMARY KEY (dept_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE admins (
    admin_id VARCHAR(15) NOT NULL,           -- 관리자 로그인 ID
    password VARCHAR(100) NOT NULL,          -- 비밀번호
    admin_name VARCHAR(30) NOT NULL,         -- 관리자 성명
    PRIMARY KEY (admin_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE students (
    student_id VARCHAR(15) NOT NULL,         -- 학번 (학생 로그인 ID로 사용)
    password VARCHAR(100) NOT NULL,          -- 비밀번호
    name VARCHAR(30) NOT NULL,               -- 이름
    dept_code VARCHAR(10),                   -- 소속 학과 코드 (외래키 변수)
    phone VARCHAR(20),                       -- 연락처
    PRIMARY KEY (student_id),
    CONSTRAINT fk_student_dept 
        FOREIGN KEY (dept_code) REFERENCES departments(dept_code) 
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO departments (dept_code, dept_name) VALUES 
('CS', '컴퓨터공학과'),
('AI', 'AI엔지니어링과'),
('AD', '디자인학과');

INSERT INTO admins (admin_id, password, admin_name) VALUES 
('admin', '1234', '최관리');

INSERT INTO students (student_id, password, name, dept_code, phone) VALUES 
('20261101', '1234', '홍길동', 'CS', '010-1234-5678'),
('20261202', '5678', '이순신', 'AI', '010-9876-5432'),
('20261303', '1111', '심청', 'AI', '010-5555-5555'),
('20261404', '2222', '강감찬', 'CS', '010-3333-4444');