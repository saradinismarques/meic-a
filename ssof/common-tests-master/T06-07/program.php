<?php

    // tests to try to avoid false positives

    // test ifelse noninterference with strings
    $k = 0;
    if ($k == $a){
        $d = "xpto1";
    } else {
        $d = "xpto1";
    }
    e1($d);

    // ... with integers
    $k = 0;
    if ($k == $a){
        $e = 1;
    } else {
        $e = 1;
    }
    e2($e);

    // ... with variables with defined value
    $k = 0;
    if ($k == $a){
        $c = 1;
        $f = $c;
    } else {
        $c = 1;
        $f = $c;
    }
    e3($f);

    // ... with the same value it had before
    $t = 0;
    if ($t == $a){
        $t = 0;
    } 
    e4($k);

    // test implicit flows with while loops
    $ii = "";
    $cc = "";
    while ($ii == $aa) {
        $cc = $cc . "";
    }
    ww($cc);

    // test nested while/if
    $mw = "";
    while ($aw == "") {
        $mw = $mw . "";
        if ($fw == "a") {
            $mw = $mw . "";
        }
        else {
            $mw = $mw . "";
        }
    }
    
    zw($mw);

?>
