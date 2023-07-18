<?php

    while (!true){
        $sink = $source;
    }

    while (false){
        $sink = $source;
    }

    $source = 0;
    $source += 1;
    while ($source != 1){
        $sink = $source;
    }

    while ($source < 1){
        $sink = $source;
    }

    while ($source > 1){
        $sink = $source;
    }

    $source++;
    $source--;
    --$source;
    ++$source;

    while ($source <= -1){
        $sink = $source;
    }

    while ($source >= 2){
        $sink = $source;
    }

    $source = ($source / 2) * 2;
    while ($source == 2){
        $sink = $source;
    }

   $source = "a" . "b" . "c";
   while ($source != "ab" . "c") {
        $sink = $source;
   }

   while(true) {
        if (false) {
            $sink = $source;
        } else {
            do_nothing();
        }
   }

?>
