# Advent-of-code
My solutions for AoC

https://adventofcode.com/

## Languages used
- [2015](2015): Python
- [2016](2016): Golang
- [2017](2017): Pascal
- [2018](2018): Python
- [2019](2019): Python
- [2020](2020): Python
- [2021](2021): Python/SQL
- [2022](2022): Pascal

## Cookiecutter template for python based solutions
How to use the cookiecutter template: `cookiecutter . -f -s dir_name=2022 day=1a`

This will generate a subdir with the new file.

Then go to the subdir and run `../get_input.bash YEAR DAY` to download your input (you might need to add your session cookie to the file `cookie.txt` first).

Test inputs can be written to files `d<DAY>.test.<#>` starting at 1, or you can write the test inputs in the python file as literals.

## Problem download
Run `../get_problem.bash YEAR DAY` to download the problem as clean html. This script uses `pup` to extract only the problem html.
Install pup: `go install github.com/ericchiang/pup@latest`
Info: https://github.com/ericchiang/pup

