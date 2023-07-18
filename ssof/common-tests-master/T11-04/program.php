<?php

    while(condition1()) {
        sink1($source1); // reached
        continue;
        sink2($source2); // never reached
    }

    while(condition1()) {
        if (condition2()) {
            break;
        }
        sink3($source4); // reached
    }

    while (condition1()) {
        if (condition2()){
            continue;
        }
        sink5($source5); // reached
    }

    while (condition1()) {
        if (condition2()) {
            continue;
            sink6($source6); // never reached
        }
        else{
            break;
            sink7($source7); // never reached
        }
        $sink8 = $source8; // never reached
    }

    // tip: break/continue in while cycle
?>