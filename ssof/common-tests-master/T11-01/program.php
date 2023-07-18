<?php

    for ($i = 1; $i < 10; ++$i) {
        $sink = source();     
    }

    for ($source1 = 1; $source1 < 10; ++$source1) {
        $sink1 = "ola";
    }

    for ($sink2 = $source2; $sink2 > 5; --$sink2) {
        break;
    }

    // tip: for statement
?>