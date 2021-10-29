empirical_incubation_dist <- function(x, date_of_onset, exposure, exposure_end = NULL) {
  # error checking
  if (!is.data.frame(x)) {
    stop("x is not a data.frame")
  }

  if (ncol(x) == 0L) {
    stop("x has no columns")
  }

  # prepare column names for transfer
  exposure <- rlang::enquo(exposure)
  date_of_onset <- rlang::enquo(date_of_onset)
  exposure_end <- rlang::enquo(exposure_end)
  end_is_here <- !is.null(rlang::get_expr(exposure_end))

  # Make sure that all the columns actually exist
  cols <- c(
    rlang::quo_text(date_of_onset),
    rlang::quo_text(exposure),
    rlang::quo_text(exposure_end)
  )
  cols <- cols[cols != "NULL"]
  if (!all(cols %in% names(x))) {
    msg <- "%s is not a column in %s"
    cols <- cols[!cols %in% names(x)]
    msg <- sprintf(msg, cols, deparse(substitute(x)))
    stop(paste(msg, collapse = "\n  "))
  }

  # Grab the values from the columns
  doo <- dplyr::pull(x, !!date_of_onset)
  expos <- dplyr::pull(x, !!exposure)

  if (!inherits(doo, "Date")) {
    msg <- "date_of_onset must be a column of Dates. I found a column of class %s"
    stop(sprintf(msg, paste(class(doo), collapse = ", ")))
  }

  if (end_is_here) {
    # We need to create the list for each date
    if (is.list(expos) || !inherits(expos, "Date")) {
      stop("if exposure_end is specified, then exposure must be a vector of Dates")
    }
    e <- expos
    ee <- dplyr::pull(x, !!exposure_end)
    expos <- vector(mode = "list", length = length(e))
    for (i in seq(expos)) {
      expos[[i]] <- seq(from = e[i], to = ee[i], by = "1 day")
    }
  }

  y <- compute_incubation(doo, expos)

  # check if incubation period is below 0
  if (any(y$incubation_period < 0)) {
    warning("negative incubation periods in data!")
  }

  return(y)
}
