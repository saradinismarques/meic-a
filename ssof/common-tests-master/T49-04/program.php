<?php
    $a = source();
    if ($a == $b) {
        $c = "1";
    } elseif ($a + 1 > $b) {
        $c = "2";
    } else {
        $d = "3";
    }
    sink($c);
?>