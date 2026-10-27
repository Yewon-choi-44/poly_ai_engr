<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
<body>
<h2><blockquote> 마당서점 주문 수정 </blockquote></h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}

	$orderid = $_POST['orderid'];
	$saleprice = $_POST['saleprice'];

	$sql = "";
	$result = mysqli_query($conn, $sql);
?>
<b><?=$sql?></b>
<br>

<?php 
	if($result) { 
		echo '<p>수정 완료</p>';
	} else { 
		echo '<p>수정 실패</p>';
	} 
?>
<br>
<a href="/orderlist_ver2.php" class="w-btn">뒤로</a>
</body>
</html>
