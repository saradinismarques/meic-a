<?php
    $sink1a = source();
    $sink1b = sani("ola", $sink1a);
    $sink2b = sani(sink2a($sink1b . "oi" . sink2a($d . "hi"), $sink1a));

    // testing concatenation with different arguments and sanitizers
?>
