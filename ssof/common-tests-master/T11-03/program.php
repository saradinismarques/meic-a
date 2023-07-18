<?php

    $a = source1();
    $a = sanitize($a);
    $a = source2($a);
    $sink1 = $a;

    // No vuln
    $b = source3();
    $b = "";
    $sink2 = $b;

    while ($c = source4()) {
        $c = sanitize($c);
    }
    $sink3 = $c;

    $d = "initialization";
    while ($sink4 = $d) {
        $d = source5();
    }
?>