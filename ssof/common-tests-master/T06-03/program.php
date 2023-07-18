<?php

    //Basic tests

    // test simple assignment inside for
    for ($i = 0; $i <= 1; $i++) {
        $b = $a;
    }

    // test assignment in initialization
    for ($c = $a, $i = 0; $i <= 1; $i++) {
        $d = $c;
    }

    // test assignment in loop part
    for ($i = 0; $i <= 2; $i++, $e = $a) {
        $f = $e;
    }

    // test condition check
    for ($i = 0; $i < 0; $i++) {
        $g = $a;
    }

    // test propagation through multiple iteration
    for ($i = 0; $i <= 0; $i++) {
        $j = $i;
        $i = $h;
        $h = $a;
    }

    // test node constrution
    for (;;) {
        $k = $a;
        break;
    }

?>
