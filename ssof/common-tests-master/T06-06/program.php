<?php
    // break node tests

    while (true) {
        break;
        $sink = source();
    }

    while (true) {
        if (condition()) {
            break;
            $sink = source();
        } else {
            break;
            $sink = source();
        }

        $sink = source();
    }

    // breaks only affect one level
    while (true) {
        while (true) {
            if (condition()) {
                if (false) {
                    $sink = source();
                } else {
                    break;
                    $sink = source();
                }

                $sink = source();
            } else {
                break;
            }

            $sink = source();
        }

        // this one will be catch
        $sink1 = source1();
    }

?>