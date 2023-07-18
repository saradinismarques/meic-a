<?php
$b = 1;
if($a){
	$a = $a + $taint;
	sink($b);
}


