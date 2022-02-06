apply_vaccine_to_population <- function(population, ndoses, threshold_age) {
  for (individual in population) {
    if (ndoses > 0) {
      if (indiv["age"] > threshold_age || indiv["isAtRisk"]) {
        if (indiv["hasFirstJab"]) {
          inject_second_jab(indiv)
        } else {
          inject_first_jab(indiv)
        }
      }
      ndoses <- ndoses - 1
    } else {
      return("No more doses")
    }
  }
}