<?php
    $a = "init";
    while (cond()){
        while(cond()){
            $a = source1();
            break 2;
            
        }
        $a = "clear"; // skipped if $a is tainted
    }

    sink($a);

    $b = "init";
    while (cond()){
        while(cond()){
            $b = sanitize1(source2());
            continue 2;
            
        }
        
        $b = sanitize2($b); // might be skipped if $a is tainted
    }
    sink($b);

    // multi-level breaks and continues
?>
