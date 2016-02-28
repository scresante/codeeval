<?php
$fname = $argv[1];
$lines = file($fname);
foreach ($lines as $line) {
  echo strtolower($line);
}

