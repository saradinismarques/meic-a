<?php
    $k = 1;
    $a = input($boo);
    if ($c == $a){
        $k -= 1;
        $d .= "value1";
    } elseif ($c < $a){
        $k += 1;
        $d = "value2";
    } else{
        $k *= 1;
        $e = "value2";
    }
    funccall1("arg1", "arg2", $k);
    funccall2("arg1", "arg2", $d);
    // testing -= operators, -= , if, else and elsifs, implicit flows
?>
