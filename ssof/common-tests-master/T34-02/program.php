<?php

    $a = source1();
    $a = sanitize($a);
    $a = source2($a);
    $sink = $a;

    // order of sources and sanitizers matters

?>