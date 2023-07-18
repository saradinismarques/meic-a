<?php

$a = 'value';
if ($a > f($c)) {
	$d = f($x);
	$e = 1337;
} elseif ($a > $d) {
	// nothing
} elseif ($a > $e) {
	$e = f($x);
} else {
	$e = 123;
}

sink($d, $e);
