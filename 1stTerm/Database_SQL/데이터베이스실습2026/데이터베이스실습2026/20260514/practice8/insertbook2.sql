use practice8;
delimiter //
CREATE PROCEDURE InsertBook2(
  IN myBookName VARCHAR(40), 
  IN myPublisher VARCHAR(40), 
  IN myPrice INTEGER)
BEGIN
  INSERT INTO Book(bookname, publisher, price)
      VALUES(myBookName, myPublisher, myPrice);
END;
//
delimiter ;

CALL InsertBook2('스포츠과학', '마당과학서적', 25000);
SELECT * FROM Book;