<?php
    $a = source1();
    while (source2()) {
        while (source3()) {
            break;
            $a = san($a);
        }
        // Should have no sanitized flows
        sink1($a);
    }
?>
