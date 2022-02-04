#' Calculate the Principal Components
#'
#' @param data matrix, or dataframe with numerical data
#' @param scalea logical value indicating whether the variables
#' should be scaled to have unit variance.
#' @param center a logical value indicating whether the variables
#' should be shifted to be zero centered.
#'
#' @return prcomp object
#'
#' @examples
#' calculatePCA(mtcars)
calculatePCA <- function(data, scale = TRUE, center = TRUE) {
  results <- prcomp(USArrests, scale. = scale, center = center)
  #reverse the signs
  # (eigenvectors in R point in the negative direction by default)
  results$rotation <- -1*results$rotation
  results$x <- -1*results$x
  results
}

#' Calculate total variance explained by each principal component
#'
#' @param pca_results prcomp object
#'
#' @return vector with explained by each principal component
#'
#' @examples
#' res <- prcomp(mtcars)
#' get_total_explained_variance(res)
get_total_explained_variance <- function(pca_results) {
  x <- results$sdev^2
  y <- sum(results$sdev^2)
  return(x / y)
}

#' Create scree plot
#'
#' @param var_explained variance explained
#'
#' @examples
#' plot_scree(c(0.8,0.1,0.005))
plot_scree <- function(var_explained) {
  nc <- length(var_explained)
  ggplot2::qplot(c(1:nc), var_explained) +
    geom_line() +
    xlab("Principal Component") +
    ylab("Variance Explained") +
    ggtitle("Scree Plot") +
    ylim(0, 1)
}

#' Test:
#' head(USArrests)
#' str(USArrests)
#' pca_results <- calculatePCA(USArrests)
#' biplot(pca_results, scale = 0)
#' plot_scree(plot_scree)
