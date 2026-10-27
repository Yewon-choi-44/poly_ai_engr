<?php
	echo '<h2>HELLO WORLD.</h2><br>';
	$str1 = "이것이 MySQL<br>"; echo $str1;
	$str2 = "PHP 프로그래밍<br>"; echo $str2;
	$str3 = "SELECT * FROM userTBL WHERE userID='JYP'"; echo $str3;
	echo '<br>';
	echo $str1;

	$jumsu = 60;
	if($jumsu >= 90) {
		echo 'A+학점';
	} else if($jumsu >= 80) {
		echo 'A학점';
	} else if($jumsu >= 70) {
		echo 'B+학점';
	} elseif($jumsu >= 60) {
		echo 'B학점';
	} else {
		echo 'F학점';
	}

	echo '<br>';
	for($i=1; $i <= 20; $i=$i+1) {
		echo $i, ' ';
	}

?>