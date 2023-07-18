<?php

$a = ~($b);
$c = !($b);
f($a, $c);

//exploit vulnerabilities with Expr_BitwiseNot and Expr_BooleanNot constructors
?>