<?php
	// Variable is unitialized, there is a vuln
	$sink1 = $a;
	// Now variable is initialized, there is no vuln anymore
	$a = 3;
	$sink2 = $a;

	// there should be only one vuln on sink1 due to unitialized var
?>