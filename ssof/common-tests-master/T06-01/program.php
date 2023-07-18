<?php

    if (!true){
        $sink = $source;
    }

    if (false){
        $sink = $source;
    }

    $source = 0;
    $source += 1;
    if ($source != 1){
        $sink = $source;
    }

    if ($source < 1){
        $sink = $source;
    }

    if ($source > 1){
        $sink = $source;
    }

    $source++;
    $source--;
    --$source;
    ++$source;

    if ($source <= -1){
        $sink = $source;
    }

    if ($source >= 2){
        $sink = $source;
    }

    $source = ($source / 2) * 2;
    if ($source == 1){
        do_nothing();
    } else {
        $sink = $source;
    }

   $source = "a" . "b" . "c";
   if ($source != "ab" . "c") {
        $sink = $source;
   }

    if (true) {
        if (((true and true) and true) or false) {
            if (true or false) {
               if (true and false) {
                   do_nothing();
               } else {
                   if (false) {
                       $sink = $source;
                   }
               }
            }
        } else {
           do_nothing();
       }
    }

?>
