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
	input.text.writable {
		background-color: #ffc107;
		border: 1px solid #ff9800;
	}
</style>
<body>
<h2><blockquote> 마당서점 도서 재고 수정</blockquote></h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}
	$sql = "SELECT * FROM Book B WHERE bookid='".$_GET['id']."'";
	$result = mysqli_query($conn, $sql);
	$row = mysqli_fetch_array($result);
?>
<form method="POST" id="register" style="width: 310px;" action="/action_updatestock.php">
    <input type="hidden" name="bookid" value="<?=$row['bookid']?>">
	<br>
	<label>Book Name </label>
    <input type="text" class="text" name="bookname" placeholder="Book Name" readonly value="<?=$row['bookname']?>">
	<br>
	<label>Book Publisher </label>
    <input type="text" class="text" name="publisher" placeholder="Publisher" readonly value="<?=$row['publisher']?>">
	</br>
	<label>Book Price </label>
    <input type="text" class="text" name="price" placeholder="Price" readonly value="<?=$row['price']?>">
	</br>
	<label>Book Stock </label>
    <input type="number" class="text writable" name="stock" placeholder="Stock" value="<?=$row['stock']?>">
	</br>
	<div>
		<a href="/booklist.php" class="form-btn">뒤로</a>
		<input type="submit" name="register" value="수정" class="form-btn" style="float: right;">
	</div>

</form>
</body>
</html>
