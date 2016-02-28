<?php
function isupper($str) {
  if ($str{0} === strtoupper($str{0})) {
    echo 'is upper';
  }
  else {
    echo 'is lower';
  }
}

$fname = $argv[1];
$lines = file($fname);
foreach ($lines as $line) {
  foreach (explode(" ",$line) as $word) {
    foreach (array($word) as $char ){
      echo $char;
      echo isupper($char);
    }
  }
}

