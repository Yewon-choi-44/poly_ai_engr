<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
<body>
<h2><blockquote> 마당서점 회원 삭제</blockquote></h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'practice3');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}
	$sql = "SELECT * FROM Customer WHERE custid=".$_GET['id'];
	$result = mysqli_query($conn, $sql);
	$row = mysqli_fetch_array($result);

	
?>
<form method="POST" id="register" style="width: 310px;" action="/action_deletecustomer.php">
    <input type="hidden" name="custid" value="<?=$row['custid'] ?>">
	<input type="text" class="text" name="name" placeholder="Name" value="<?=$row['name']?>" readonly><br>
	<input type="text" class="text" name="address" placeholder="Address" value="<?=$row['address']?>" readonly></br>
	<input type="text" class="text" name="phone" placeholder="Phone" value="<?=$row['phone']?>" readonly></br>
	<input type="text" class="text" name="email" placeholder="Email" value="<?=$row['email']?>" readonly></br>
    <div>
	<a href="/customerlist3.php" class="form-btn">취소</a>
	<input type="submit" name="register" value="삭제" class="form-btn" style="float: right;">
    </div>
</form>

</body>
</html>
