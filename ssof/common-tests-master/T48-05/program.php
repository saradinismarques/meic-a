<?php


    $x = source();
    $y = s($x);
    $v = 1;
    $j = e($y, e($v), $x, $v);
    $v += $x;
    $y--;
    sink1($y);
    --$v;
    sink2($v);
    $sink3 = $j;

    // test increments and assignOps | assignOps can change the taint of a symbol while increments cant
?>