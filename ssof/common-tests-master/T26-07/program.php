<?php

   $c = b();
   if ($c < 3) {
      f($a);
   }
   elseif ($c == 3) {
      g($a);
   }
   else {
      h($a);
   }

   // tip: sources, sanitizers and sinks can appear inside branches, and they can be nested

?>
