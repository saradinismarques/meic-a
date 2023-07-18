<?php

    if ($source1){
        sink1();
        $a=$source1;
    }elseif($source2){
        sink2();
        $a=$source2;
    }elseif($source3){
        sink3();
        $a=$source3;
    }else{
        sink4();
    }
    $sink = $a;

    // elseifs implicit flows
?>