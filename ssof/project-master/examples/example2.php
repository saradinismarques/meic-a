<?php
    $u = $_GET['username'];
    $p = $_GET['password'];
    $q = "SELECT * FROM users WHERE user='" . $u . "' AND password='" . $p . "'";
    $query = mysql_query($q);

?>