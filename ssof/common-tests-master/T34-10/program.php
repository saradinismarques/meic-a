<?php
    $a = "initialized";
    $b = "initialized";
    $c = "initialized";
    $d = "initialized";
    
    while (source1() xor ($c = sanitize(source2()))){ // condition is checked after continue
        $a = "implicit";
        $b = source1();
        if (cond()) {
            $d = source2();
            continue;
        }
    
        $a = "clean";
        $b = "clean"; // might be reached or skipped
        $c = "clean";
        
        $sink4 = $d;
        sink3($d); // vuln happens on iterations after continue 
    }

    sink1($a);
    sink1($b);
    sink2($c);


    while (condition1()) {

        if (condition2()) {
            continue;
            sink4(source4()); // never reached
        }
        else{
            continue;
            sink4(source4()); // never reached
        }
        sink3(source3()); // never reached

    }

    // continue paths
?>
