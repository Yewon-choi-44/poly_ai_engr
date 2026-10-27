<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="book.css" rel="stylesheet">
</head>
<body>
<h2 class="styled-header">마당서점 도서목록</h2>
<?php
	$conn = mysqli_connect('localhost', 'madang', 'madang', 'bookstore');
	if (!$conn){
		echo 'Connection Error';
		echo mysqli_connect_error();
		exit();
	}

	$sql = "SELECT * FROM Book";
	$result = mysqli_query($conn, $sql);

	echo '<table class="styled-table"><thead><tr><td>BOOKNAME</td><td>PUBLISHER</td><td>PRICE</td></tr></thead><tbody>';
	
	while($row = mysqli_fetch_array($result)) {
		/*$row = {
			'bookid': '1',
			'publisher': '축구책',
			'bookname': '축구책'
		}*/
		echo ('<tr class="active-row"><td><b>
			<a href="bookview.php?id='.$row['bookid'].'">'
			.$row['bookname'].'</a></b></td><td>'
			.$row['publisher'].' </td><td> '
			.$row['price'].'</td></tr>'); 
	}
	echo '</tbody></table><p>';

?>
</body>
</html>
