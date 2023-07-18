<?php

    while ($source1){
        sink1();
        while($source2){
            sink2();
            while ($source3){
                sink3();
            }
        }
    }

    // implicit flows in nested whiles
?>