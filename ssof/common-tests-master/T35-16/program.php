<?php

    $a = source();
    $a = "OK";
    sink($a);
    $a = $d;
    echo $a, source();

    // $a is clean for the first sink but is tainted for echo.

?>
