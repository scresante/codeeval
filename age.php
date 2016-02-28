<?php
$fname = $argv[1];
$lines = file($fname);
foreach ($lines as $value) {
     if ($value < 0 || $value > 100 ) {
         echo 'This program is for humans';
     } elseif ( $value <= 2 ) {
         echo 'Still in Mama\'s arms';
     } elseif ( $value <= 4 ){
         echo 'Preschool Maniac';
     } elseif ($value <= 11) {
         echo 'Elementary school';
     } elseif ($value <= 14) {
         echo 'Middle school';
     } elseif ($value <= 18) {
         echo 'High school';
     } elseif ($value <= 22) {
         echo 'College';
     } elseif ($value <= 65 ){
         echo 'Working for the man';
     } elseif ($value <= 100) {
         echo 'The Golden Years';
     }

     echo PHP_EOL;
 }
echo "";
 
?>

