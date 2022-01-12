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

# Snippets
## `apply_vaccine.R`
- Hard to grasp what function does at first glance
- Combination of loop and nested conditional could be "flattened"
- It's often useful to use helper function to extract conditions
  ```R
  is_eligible <- function(individual, threshold_age) {
      return(indiv["age"] > threshold_age || indiv["isAtRisk"])
  }
  ```
## `empirical_incubation_dist.R`

- Function is long
- Could try and ientify independant blocks of code that could be
  extracted into functions.
- Name of function could be more descriptive, a docstring would help
- code is rather well formatted and steps of calculation are clear
- Good error checking
- Some variable could use more descriptive names (e.g. `doo`)
