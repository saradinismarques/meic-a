<?php

$a = "";

// $i is unitialized
switch ($i) {
    case 0:
        $a = $b; // $b -> $a
        break;
    case 1:
        $a = $c; // $c -> $a
        break;
    case 2:
        $a = $d;
        break;
}

e($a)

?>
