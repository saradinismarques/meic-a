<?php
    $a = "initialized";
    $b = "initialized";
    $c = "initialized";
    $d = "initialized";

    while (source1() xor ($c = sanitize1(source2()))){ // condition is not checked after continue
        $a = "implicit";
        $b = source1();
    
        if (cond()) {
            $c = sanitize2(source2());
            $d = source3();
            break;
        }
    
        $a = "clean";
        $b = sanitize1(source1()); // might be reached or skipped
        $c = "clean";
        
        $sink4 = $d; // unreachable if $d is tainted

        sink3($d); // unreachable if $d is tainted
    }

    sink1($a);
    sink1($b);
    sink2($c);


    while (condition1()) {

        if (condition2()) {
            break;
            sink4(source4()); // never reached
        }
        else{
            break;
            sink4(source4()); // never reached
        }
        sink3(source3()); // never reached

    }

    // break paths
?>
