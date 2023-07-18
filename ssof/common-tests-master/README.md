# Community Tests Repository

Welcome to the Community Repository for Testing the Projects of the Software Security course 2022/23.

Note that __this repository is not supervised by the lecturers of the course, hence no guarantees of correctness of the provided examples are provided__. Apply your best judgement when using these tests.

## Submitting a test

If you want to submit a test, just create folder `TXX-NN` where `XX` is your group number and `NN` is the test sequence number for your group.  
For example, the 3rd test submitted by group 47 should be in folder `T47-03`.

1. Add the following files to that folder

   - `program.json` with the input slice  
   - `patterns.json` with the patterns to verify  
   - `output.json` with the expected output  
   - `program.php` with the original PHP slice for convenience of reading

2. Commit the test to the repository, with a brief commit message explaining the goal of the test.

### Before submitting a test

Before submitting a test please check if it is syntactically correct:

    python3 validate.py -p <path_to_test>/patterns.json -o <path_to_test>/output.json

## Running a test

To run a test you should run:

    <your_program> <path_to_test>/program.json <path_to_test>/patterns.json

where

- `<your_program>` is the command to run your project (e.g., `python3 php-analyser.py` or `java php-analyser`, or `...`), and  
- `<path_to_test>` is the path to the test folder you want to use (e.g., `T47-03`).

### Checking output

You can also use `validate.py` to check the equality with the intended output (notice that the order of the lists may differ hence `diff` may return incorrect results). To compare your result with the one in `<path_to_test>/output.json` use:

    python3 validate.py -o <path_to_your_output>/program.output.json -t <path_to_test>/output.json

## Spotting incorrect Outputs/Mistakes

In case you find a mistake, please submit an issue detailing the error and assign it to the person that submitted the original test.

If it is clear that it is an error, you can also submit a pull request with the fix and commit message `fixes #Y` where Y is the issue number.
