<?php
	/// the following lines have no vulnerabilities, but need to be parsed successfully
	// literals
	$a = 3;
	$a = "test";
	$a = 3.14;
	$a = false;

	// const
	define("TEST", 3);
	$a = test;

	// echo
	echo "Hello", " ", "World!";

	/// the following lines should all result in vulnerabilities of source "$_src"
	// bitwise operation
	$_src = 1;
	$S1 = 0 | $_src;

	// boolean not
	$S2 = !$_src;

	// increment/decrement
	$S3 = $_src++;
	$S4 = ++$_src;
	$S5 = $_src--;
	$S6 = --$_src;

	// array dim fetch
	$S7 = $_GET["username"];

	// assign op
	$S8 = 0;
	$S8 += $_src;
?>