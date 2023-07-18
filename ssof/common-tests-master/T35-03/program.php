<?php

$d = "";
$a = ~($b);
$c = $a;
$a = $d;
f($a);
g($c);

//a variable can be tainted and then non tainted

?>
