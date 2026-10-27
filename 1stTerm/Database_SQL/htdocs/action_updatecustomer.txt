<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
<body>
<h2><blockquote> 마당서점 회원 수정 </blockquote></h2>
<?php

	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}

	$custid = $_POST['custid'];
	$address = $_POST['address'];
	$phone = $_POST['phone'];
	$email = $_POST['email'];

	$sql = "UPDATE customer SET address='$address', phone='$phone', email='$email' WHERE custid=$custid";
	$result = mysqli_query($conn, $sql);

?>

<b><?=$sql?></b>
<br>

<?php 
	if($result) { 
?>
		<p>수정 완료</p>

<?php 
	} else { 
?>
		<p>수정 실패</p>
<?php 
	} 
?>

<br>
<a href="/customerlist.php" class="w-btn">뒤로</a>

</body>
</html>
