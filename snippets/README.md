# `apply_vaccine.R`
- Hard to grasp what function does at first glance
- Combination of loop and nested conditional could be "flattened"
- It's often useful to use helper function to extract conditions
  ```R
  is_eligible <- function(individual, threshold_age) {
      return(indiv["age"] > threshold_age || indiv["isAtRisk"])
  }
  ```
# `empirical_incubation_dist.R`

- Function is long
- Could try and ientify independant blocks of code that could be
  extracted into functions.
- Name of function could be more descriptive, a docstring would help
- code is rather well formatted and steps of calculation are clear
- Good error checking
- Some variable could use more descriptive names (e.g. `doo`)
