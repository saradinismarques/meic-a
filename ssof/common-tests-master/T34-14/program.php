<?php
    $a = sanitizer1(source());
    implicit_source() and ($a = sanitizer2($a));
    sink($a);

    // short-circuit operators can create different flows

?>
