# Project Validator

Following our preliminary evaluation of the experimental part of the projects we identified that many groups did not follow the specifications provided in the project, in particular name of the tool, output folder, naming of the output files, among others. This leads to a fail in the automatic evaluation process that we cannot possibly deal with manually within the available time-frame.

In order to allow us to properly evaluate the projects that do not adhere to these we are allowing groups to make changes to their projects and perform new commits to their repos where these issues are fixed. This possibility is open until **Tuesday, January 31, 2023, 5pm**.

For the full details, methodology to do so, and what is allowed and disallowed, please check the info below.

## Specification

Recall the specifications for the tool and the output:

- Your project file should be called `php-analyser.py`.
- The tool should be called in the command line with two arguments: `<slice>.json` and `<patterns>.json`.
- The tool should produce the output related to the `<slice>.json` being run and save it to a file named `<slice>.output.json`
- The output file should be saved in the `./output/` folder.
- Ensure the output is in the EXACT format specified in the project statement.
  - Double-check the spelling of fields such as `source` instead of `sources`.

## Validation

To ensure that the output is generated correctly perform the following actions:

1. Copy the `tests` folder, and `autotest.sh` and `validate.py` scripts to the directory of your project.
2. Run the `autotest.sh` script.
3. If the script runs without errors,
    - the output has been generated with the correct name in the `output/` folder, and
    - the **output format** is correct.
4. You may also check if the solution is correct. For that, you should answer `y` when prompted for `check solution (y/n)`.

If your project was NOT made in python3, you have to uncomment the appropriate line in the `autotest.sh`. YOU SHOULD NOT MAKE ANY OTHER CHANGE TO THE SCRIPT.

## Acceptable Changes

The changes to the project that are accepted are all those that enable the proper execution of step 3. above without errors.

If your group has identified other small errors that impact the fair assessment of your project, eg, an `=` instead of `==`, you may message Pedro Adão asking for permission to fix such issue also.

**Any change that is not in one of this 2 categories will result in the exclusion from this revision process.**
