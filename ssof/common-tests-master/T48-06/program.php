<?php

$a = "switch";

switch ($u) {
    case 0:
        $a = $source1; 
        break;
    case 1:
        $a = $source2; 
        break;
    case 2:
        $a = $source3;
        break;
    case 3:
        $a = $source4;
        break;
}

sink($a)

?>