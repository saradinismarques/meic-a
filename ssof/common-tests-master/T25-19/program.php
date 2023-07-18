<?php

switch ($imp1) {
    case s($source1):
        $b = $source1;
        $c = $source2;
    case s($b):
        $a = $b;
        $c = 1;
        break;
    default:
        $a = $c;
}
$sink = $a;

?>