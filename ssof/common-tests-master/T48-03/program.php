<?php

   $a = source($boo);
   if ($c == $a){
      $d = "xpto1";
   } elseif ($c < $a){
      $d = "xpto2";
   } else{
      $e = "xpto3";
   }
   sink1($d, "boo");
   $sink2 = $e;

   // testing ifs, elseif and different possible outcomes with implicit flows

?>