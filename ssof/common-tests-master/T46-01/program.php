<?php
    $u = $_GET['username'];
    $p = $_GET['password'];
    $q = "SELECT * FROM users WHERE user='" . $u . "' AND password='" . $p . "';";
    $q2 = "SELECT * FROM users WHERE user='" . mysql_real_escape_string($u) . "' AND password='" . mysql_real_escape_string($p) . "';";
    $query = mysql_query($q);
    $query = mysql_query($q2);
    $q2 += $q;
    $query = mysql_query($q2);
    echo $q2;
?>
