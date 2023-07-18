<?php
    $a = "";
    $b = "";
    while (cond()) {
        $a = $b;
        $b = source1();
        if (t()) {
            continue;
        } 
        $b = "";
    }
    sink1($a);
?>
