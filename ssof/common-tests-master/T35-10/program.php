<?php
	if(true) {
		$d = 1;
		if(false) {
			$c = 3;
		} else {
			$c = 4;
		}
	} else {
		$c = 2;
		if(true) {
			$d = 5;
		} else {
			$d = 6;
		}
	}
	e($d, $c)

	// $d and $c will always get assigned, so no vulnerabilities should exist due to unitialized vars
?>

