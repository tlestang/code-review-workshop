# Practices ("smells") to illustrate

4 code review viewpoints:
- Design (OOP principles, Design Patterns, YAGNI)
- Readability & Maintainability
- Functionality
  - Do the code does what it is supposed to do?
  - Are there tests, are they readable?
  - Are tests correct and testing the right things?
- Performance

List of discrete practices to illustrate in snippets:
- [ ] Inaccurate or misleading naming (**R**)
- [ ] Inaccurate, misleading or inexistent comment(s) (**R**)
- [ ] Long function / class (**R**, **D**)
- [ ] Nested conditionals (**R**)
- [ ] Complex conditional statement (**R**)
- [ ] Wrong data structure (**R**, **P**)
  - Ex: numpy array instead of list, dict instead of dataframe
- [ ] Duplicated code (**R**, **D**)
- [ ] You ain't Gonna Need It (YAGNI) over-engineering (**D**, **P**)
- [ ] Implementing what would be provided by a library (**R**, **P**)
- [ ] Routine with weak cohesion (**D**, **R**)
  - For instance routine that does multiple operations, each operating
    on different data.
- [ ] Routines with unacceptable coupling
  - For instance global data coupling or control coupling
- [ ] Variables declared and initialized for from use
  

# Snippets
## `apply_vaccine.R`
### Docstrings and comments
- No docstrings. Questionable if `lookup_vaccine_name` needs one, but
  `apply_vaccine_to_population` is complex and takes three different parameters.
- Comments could help clarifying the logic of `apply_vaccine_to_population`.
- Use of `collections.Counter` is made clear with comment.
### Function `lookup_vaccine_name`
- Function takes whole `individual` structure as parameter but only
  uses a couple of fields. Data required by `lookup_vaccine_name` is
  not clear from its definiton. Example of questionable
  structured-data coupling: could take jab location and jab date as
  parameters instead of `individual` object.
- Names are clear and consistent
### Function `apply_vaccine_to_population`
- Hard to grasp at first glance what function does. Mostly because of
  nested conditionals and cmplex condition.
- Threefold conditional should be flattened by returning as soon as
  possible (guard clauses).
- Condition on line 17 could be extracted to boolean function `isEligible`.
- Good use of custom exception.
- No apparant guarantee that vaccine wouldn't be given to already
  double-jabbed individual. Could it be a problem? 
### General
- `individual` could a class instance rather than a dictionary, with methods to inject jabs.
- Combination of loop and nested conditional could be "flattened".
- Good use of `collections` module
- Would it make sense to have parameters like `threshold_age` or
  `ndoses` as command line arguments?
- Good use of `collections` module. Commment is useful as function is
  likely unknown to a lot of readers.

## `empirical_incubation_dist.R`

- Function is long
- Could try and ientify independant blocks of code that could be
  extracted into functions.
- Name of function could be more descriptive, a docstring would help
- code is rather well formatted and steps of calculation are clear
- Good error checking
- Some variable could use more descriptive names (e.g. `doo`)


## `code_to_review1.py`

- undocumented, or not properly documented functions
- lack of descriptiod of expected input / output, returns
- non-significant naming of the functions
- unused functions
- commented out code
- messed up local and global variables
- (+) comments in critical places of the code
- (+) assertion checks for types of critical variables
- testing not in `if __name__` block (or a separate scirpt)
- (+) test cases included
- function imports all over the place

## `code_to_review2.py`

- (+) logical use of the object orented structure
- testing not in `if __name__` block (or a separate scirpt)
- (+) test cases included
- function imports all over the place
- types of variables / methods included
- is making `Analysis` class abstract the best choice? Now programmer
needs to create a separate class for every analysis, maybe better
to keep them as objects and define generic method?
- tests not comprehensive
- unspecific names of the variables (`for a in ...`)
- (+) docstrings included ...
- ... but too short, not really meaningful

## `code_to_review3.R`

- (+) description of the general idea of the script
- undocumented function
- messed up local and global variables
- magic numbers (`population_within_10_km+0.1`, `shape = 16`, `fill = "#2b272e"` etc.)
- (+) long and meaningful variables names
- constants (`col_palette`) not separetd from the rest of code
- complicated nested fucntion calls `plot.list <- lapply(...`
- long lines
- inconsistent use of aggignement operators (`<-` and `=`)
- repeated lines (possible to wrap into functions)
