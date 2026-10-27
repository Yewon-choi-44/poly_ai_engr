<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
<style>
	body {
		width: 400px;
	}
	label {
		padding-left: 12px;
	}
</style>
<body>
<h2><blockquote> 마당서점 도서 삭제</blockquote></h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}
	$sql = "SELECT * FROM Book WHERE bookid='".$_GET['id']."'";
	$result = mysqli_query($conn, $sql);
	$row = mysqli_fetch_array($result);
	$stock = 0;
	if(isset($row['stock'])) {
		$stock=$row['stock'];
	}	
?>
<form method="POST" id="register" style="width: 310px;" action="/action_deletebook.php">
	<label>Book ID </label>
    <input type="text" class="text" name="bookid" placeholder="BookID" readonly value="<?=$row['bookid']; ?>">
	<br>
	<label>Book Name </label>
    <input type="text" class="text" name="bookname" placeholder="Book Name" readonly value="<?=$row['bookname']; ?>">
	<br>
	<label>Book Publisher </label>
    <input type="text" class="text" name="publisher" placeholder="Book Publisher" readonly value="<?=$row['publisher']; ?>">
	<br>
	<label>Book Price </label>
    <input type="text" class="text" name="price" placeholder="Price" readonly value="<?=$row['price']; ?>">
	</br>
	<label>Book Stock </label>
    <input type="text" class="text" name="stock" placeholder="Stock" readonly value="<?=$stock ?>">
	</br>
    <div>
	<a href="/booklist.php" class="form-btn">취소</a>
	<input type="submit" name="register" value="삭제" class="form-btn" style="float: right;">
    </div>
</form>
</body>
</html>
