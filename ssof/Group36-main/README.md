### Running the tool

The tool should be called in the command line. All input should be encoded in [JSON](http://www.json.org/).

The program should receive two arguments:

- the name of the JSON file containing the program slice to analyse, represented in the form of an Abstract Syntax Tree;
- the name of the JSON file containing the list of vulnerability patterns to consider.

The tool is called in the command line by:

    $ python3 php-analyser.py slice.json patterns.json

Where: 
1. `<slice>.json` and  `<patterns>.json` represent the two arguments mentionated before
2. the output file will be created as `<slice>.output.json` at `./output/` folder.

### Validate the tool

The tool is validated in the command line by:

    $ python3 validate.py -p patterns/ -o outputs -t output -a slices_ast
