drop procedure if exists test_join_loop;
drop procedure if exists test_subquery_loop;
DELIMITER $$

CREATE PROCEDURE test_subquery_loop()
BEGIN
  DECLARE i INT DEFAULT 0;
  DECLARE start_ts DATETIME(6);
  DECLARE end_ts DATETIME(6);

  -- 임시 테이블 생성
  CREATE TEMPORARY TABLE IF NOT EXISTS dummy_result (
    name VARCHAR(255),
    total INT
  );

  TRUNCATE TABLE dummy_result;

  SET start_ts = CURRENT_TIMESTAMP(6);

  WHILE i < 10000 DO
    INSERT INTO dummy_result (name, total)
    SELECT
      (SELECT name FROM customer c WHERE c.custid = od.custid),
      SUM(saleprice)
    FROM orders od
    GROUP BY od.custid;

    SET i = i + 1;
  END WHILE;

  SET end_ts = CURRENT_TIMESTAMP(6);

  -- 결과 시간만 출력
  SELECT TIMEDIFF(end_ts, start_ts) AS total_elapsed;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE test_join_loop()
BEGIN
  DECLARE i INT DEFAULT 0;
  DECLARE start_ts DATETIME(6);
  DECLARE end_ts DATETIME(6);

  -- 임시 테이블 생성 (결과 무시용)
  CREATE TEMPORARY TABLE IF NOT EXISTS dummy_result (
    name VARCHAR(255),
    total INT
  );

  TRUNCATE TABLE dummy_result;

  SET start_ts = CURRENT_TIMESTAMP(6);

  WHILE i < 10000 DO
    INSERT INTO dummy_result (name, total)
    SELECT c.name, SUM(od.saleprice)
    FROM orders od
    JOIN customer c ON c.custid = od.custid
    GROUP BY od.custid;

    SET i = i + 1;
  END WHILE;

  SET end_ts = CURRENT_TIMESTAMP(6);

  -- 실행 시간만 출력
  SELECT TIMEDIFF(end_ts, start_ts) AS total_elapsed;
END$$

DELIMITER ;