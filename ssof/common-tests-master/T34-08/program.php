<?php

    $source && sink1(); // implicit flows
    $source  || sink2();
    $source and sink3();
    $source or  sink4();

    $source xor sink5(); // no implicit flow

    // short-circuit operators can generate implicit flows 
?>