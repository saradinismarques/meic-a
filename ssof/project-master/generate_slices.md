# Generate AST of PHP Slices

Your program should read from a text file (given as first argument in the command line) the representation of a PHP slice in the form of an Abstract Syntax Tree (AST).

In this project we will use the AST represented in JSON, using the same structure as in [PHP Parser library](https://github.com/nikic/PHP-Parser).

## Install the PHP Parser

```bash
### Install php8.1 for Ubuntu <= 20.04
sudo apt install lsb-release ca-certificates apt-transport-https software-properties-common -y
sudo add-apt-repository ppa:ondrej/php

sudo apt update
sudo apt install php8.1
php --version
sudo apt install php8.1-cli php8.1-common

### Install composer
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

### Install parser
php composer.phar require nikic/php-parser
```

## Generate AST

To generate the AST of a PHP slice execute

```bash
php ./slice-parser.php <slice>.php > <slice>.json
```

where `slice-parser.php` is the file below:

```php
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
```
