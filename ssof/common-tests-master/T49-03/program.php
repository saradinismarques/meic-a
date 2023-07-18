<?php
    $a = 0;
    switch ($b) {
        case 0:
            $a = -source(); 
            break;
        case 1:
            $a = +source(); 
            break;
    }
    sink($a)
?>