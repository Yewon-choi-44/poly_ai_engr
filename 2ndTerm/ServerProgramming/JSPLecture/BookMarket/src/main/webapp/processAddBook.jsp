<%@page import="java.util.Enumeration"%>
<%@page import="com.oreilly.servlet.multipart.*"%>
<%@page import="com.oreilly.servlet.*"%>
<%@page import="dto.Book"%>
<%@page import="dao.BookRepository"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>신규도서등록</title>
</head>
<body>
	<% 
	request.setCharacterEncoding("UTF-8");

	String filename = "";
	String realFolder = "C:\\Users\\AI-00\\Desktop\\하이테크_\\2ndTerm\\ServerProgramming\\JSPLecture\\BookMarket\\src\\main\\webapp\\images";
	
	int maxSize = 5 * 1024 * 1024;
	String encType = "utf-8";
	
	
	MultipartRequest multi = new MultipartRequest(request, realFolder, maxSize, encType, new DefaultFileRenamePolicy());
	
	String bookId = multi.getParameter("bookId"); 
	String name = multi.getParameter("name"); 
	String unitPrice = multi.getParameter("unitPrice"); 
	String author = multi.getParameter("author"); 
	String publisher = multi.getParameter("publisher"); 
	String releaseDate = multi.getParameter("releaseDate"); 
	String description = multi.getParameter("description"); 
	String category = multi.getParameter("category"); 
	String unitInStock = multi.getParameter("unitInStock"); 
	String condition = multi.getParameter("condition"); 

	Enumeration files = multi.getFileNames();
	String fname = (String) files.nextElement();
	String fileName = multi.getFilesystemName(fname);
	
	Integer price;
	
	if (unitPrice.isEmpty())
		price=0;
	else
		price=Integer.valueOf(unitPrice);
	
	long stock;
	
	if (unitInStock.isEmpty())
		stock=0;
	else
		stock=Long.valueOf(unitInStock);
	
	BookRepository dao = BookRepository.getInstance();

	Book newBook = new Book();
	newBook.setBookId(bookId);
	newBook.setName(name);
	newBook.setUnitPrice(price);
	newBook.setAuthor(author);
	newBook.setPublisher(publisher);
	newBook.setReleaseDate(releaseDate);
	newBook.setDescription(description);
	newBook.setCategory(category);
	newBook.setUnitInStock(stock);
	newBook.setCondition(condition);
	newBook.setFilename(fileName);

	dao.addBook(newBook);
	
	response.sendRedirect("books.jsp");
%>
</body>
</html>