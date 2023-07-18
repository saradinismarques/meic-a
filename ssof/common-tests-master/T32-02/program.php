<?php
  	$e = GET_CALL('email');
   	$p = GET_CALL('password');

   	$q1 = "SELECT * FROM user WHERE email='" . $e . "' AND password='" . $p . "'";
	$q2 = mysql_query($q1);
?>