<?php

$a = "";
switch (source_implicit1()) {
    case 1:
        $a = source1();
    case s(source_implicit2()):
        $a = s(source2() . $a);
        break;
    case 2:
        $a = source3();
        break;
}

sink1($a)
// switch condition and cases generate implicit flows
?>
