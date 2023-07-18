<?php

require 'vendor/autoload.php';
use PhpParser\ParserFactory;

$file_name = $argv[1];
$myfile = fopen($file_name, "r");
$code = fread($myfile,filesize($file_name));
fclose($myfile);

$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);

try {
    $stmts = $parser->parse($code);

    echo json_encode($stmts, JSON_PRETTY_PRINT), "\n";
} catch (PhpParser\Error $e) {
    echo 'Parse Error: ', $e->getMessage();
}
