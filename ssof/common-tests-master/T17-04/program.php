<?php

if ($g == 0){
    $a = "";
} elseif ($g == 1) {
    $a = $b;    // $a gets tainted by $b
} else {
    $a = $d;    // $a gets tainted by $d
}
e($a);  // $a reaches a sink, 2 tainted flows

?>