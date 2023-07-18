<?php
    $a = source("ola");
    $b = -sanitizer("oi", sink($a), $a);
    sink($b);
?>