<?php
$fname = $argv[1];
$lines = file($fname);
foreach ($lines as $value) {
    $value = strtolower( preg_replace("/[^a-zA-Z]/", "", $value) );
    echo $value;
    echo PHP_EOL;
}
echo "";
?>
