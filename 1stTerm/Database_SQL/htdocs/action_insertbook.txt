<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
<body>
<h2><blockquote> 마당서점 도서 등록 </blockquote></h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}

	$bookname = $_POST["bookname"]; //데이터베이스
	$price = $_POST["price"]; //30000
	$publisher = $_POST["publisher"]; //폴리텍
	$stock = $_POST["stock"]; // 100

	$sql = "INSERT INTO Book SET bookname='$bookname', publisher='$publisher', price='$price', stock=$stock";
	echo $sql;
	echo '<br>';
	$result = mysqli_query($conn, $sql);
	if($result) {
	    echo '도서 등록 성공';
	}
	else {
	    echo '도서 등록 실패';
	}	
?>
<br><a href="/booklist.php" class="w-btn">목록</a>
</body>
</html>
