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


## `linear_regression.py` - runs

- undocumented, or not properly documented functions
- lack of descriptiod of expected input / output, returns
- non-significant naming of the functions (mention PEP8, but also that it's okay to work out a lab's convention)
- unused functions
- commented out code
- messed up local and global variables
- (+) comments in critical places of the code
- (+) assertion checks for types of critical variables
- but suggest using try/except block instead (assert statements in non-test code should have a very limited use)
- print statements should be limited, rather `logging` module for debugging (i.e. line 46)
- testing not in `if __name__` block (or a separate scirpt)
- (+) test cases included
- function imports all over the place

## `reporting_script.py` - runs

- (+) logical use of the object orented structure
- testing not in `if __name__` block (or a separate scirpt)
- (+) test cases included
- function imports all over the place
- types of variables / methods included
- is making `Analysis` class abstract the best choice? Now programmer
needs to create a separate class for every analysis, maybe better
to keep them as objects and define generic method?
- `Analysis.complete` boolean could be set internally in run?
- tests not comprehensive
- unspecific names of the variables (`for a in ...`)
- (+) docstrings included ...
- ... but too short, not really meaningful

## `volcano_analysis.R` - runs

- (+) description of the general idea of the script
- undocumented function
- messed up local and global variables
- magic numbers / values (`population_within_10_km+0.1`, `shape = 16`, `fill = "#2b272e"` etc.)
- (+) long and meaningful variables names
- constants (`col_palette`) not separetd from the rest of code (capital letters)
- complicated nested fucntion calls `plot.list <- lapply(...`
- long lines
- complicated ggplot call (possible to break it down)
- inconsistent use of aggignement operators (`<-` and `=`)
- repeated lines (possible to wrap into functions)
- suggest separating cleaning data and plotting to two separate scripts (or at least making secitons in comments)

## `pca_functions.R` - runs

- (+) good documentation
- (+) code is rather clear and logically separated into separate functions
- (+) function names are clear and follow HW style-guide
- some variables could be better named (`nc`)
- although some returns could be more elaborated on
- testing could be done separately (or moved to the testing function) - not commented
- messed up local and global variables
- imports (`ggplot2`) should be moved to the top of the script (unless it's a package, then to DESCRIPTION and `@import` statement should be used)
- in fact `plot_scree` in the current format wouldn't work without importing `ggplot2` (as not only `qplot`, but also `geom_line`, etc. come from the package)
- (optional) `get_total_explained_variance` could be one-liner
- inconsisted use of `return`, R by default returns whatever is in the last line of the function


## `graph_neighbourhood.py`

**Pros**

- Good code formatting and organisation
- General good naming for variables and functions
- Well use of `__main__` block to organise the statements to be executed when running the module directly.
- Good use of `ArgumentParser` to clearly define the CLI (`Command Line Interface`)

**Cons**
- Module is not self-consistent (iow _lack of encapsulation_ in the `main` block)
    * Core function and processing should be abstracted into an importable function!
- Unused imports
- Lack of docstrings, and documentation
    * There are triple-quotes in the top of the module, but empty. Also having this a `main` block usually implies that some documentation should be added/needed.
    * Documentation of CLI is poor and sometimes missing
    * Complete lack of docstring in `neighbourhood` function
    * Only partial use of `type-hints` in function signature
    * Function signature doc is wrong (i.e. `return type`)
- `neighbourhood` function implementation is very cryptic
    * Code doesn't adhere to the `explicit is better than implicit` rule from the _Zen of Python_
    * 8 possible directions of indices (e.g. `n, s, ne, sw, ..`) should be easily generated by calling `itertools.product`
    * `filter` with `starmap` is simply undeadable to be comprehensible. Explicit `for` and `if` constructs should be used, instead!

**AOB**

- `logfile` is opened, and never closed!
- `nn` variable name is misleading, and not communicative enough. Also see last `for` loop
- call to `neighbourhood` in the inner `for-loop` should be cached and improved 
    * maybe use `functools.partial` to fix call with `borders` parameter



## `plotting.py`

**Pros**

- Good code formatting, and organisation
- Clear module docstring
- Generally good variable names (but still requires improvements)

**Cons**

- Globals require revision and improvements:
    * `CHART_FOLDER` points to a local path to the machine
    * `default_color_map` (which is supposed to be a CONSTANT) doens't adhere with PEP8 - iow. should be all uppercase.
- `bar_plot` function is a mess :D
    * long list of parameters (lack of encapsualtion)
    * duplicated code (e.g. see lines `157-182`)
    * function with no-effect (more later)
    * lack of cohesion (mix of data processing and data visualisation)
    * long list of parameters
    * outdated docstring
    * name of parameters should be improved (e.g. `width` refers to bar width, but after `figsize` might be confused with `figure width`.)
    * default values for some parameters are mostly `None` but should instead comply with their corresponding `type-hints`.
    * very long implementation - should be better structured
    * also, plotting function should always return the `Axis` object (e.g. see `pd.DataFrame.plot`) rather than just _plotting_. In this case, also the last `if-branch` with `filename` should be removed.


## `track_reconstruction.py`

**Pros**

- code formatting, and import organisation

**Cons** (function `fit_data`)

- lack of any documention of docstring
    * function parameters should benefit from use of `type-hint` for parameters, as well as for the return type
- (in fact) type-hinting would have clarified the complete lack of encapsulation in the return values (as well as parameters)
- lack of encapsulation in parameters is also reflected on the many cases of duplicated code;
- there is lack of comments (and inline ones are quite poor)
    * no clear explanation nor rationale on conditions (e.g. what do conditions on `L59,69` mean?)
- some `print` and `debug` code should be removed
- no clear definition of what the function is doing (following from _lack of documentation_)
- variable names should be improved