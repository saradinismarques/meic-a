<?php
    // implicit flow taints all function calls, even with no args
    if ($source){
        sink();
    }

    // implicit flows in nested whiles
    while ($source1){
        sink1();
        while($source2){
            sink2();
            while ($source3){
                sink3();
            }
        }
    }


?>