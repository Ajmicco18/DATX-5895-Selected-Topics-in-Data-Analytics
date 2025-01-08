#Question 1

library(data.table)
products <- fread("/anvil/projects/tdm/data/icecream/combined/products.csv")
reviews <- fread("/anvil/projects/tdm/data/icecream/combined/reviews.csv")
unique(trimws(unlist(strsplit(products$ingredients[1], ",|\\(|\\)"))))
getingredients <- function(x){
    unique(trimws(unlist(strsplit(x, ",|\\(|\\)"))))
}
barplot(tail(sort(table(unlist(sapply(products$ingredients, getingredients),use.names=FALSE))),n=10))
table(reviews$stars)
plot(table(reviews$stars), type="o",xlab="stars", ylab="frequency", main="Distribution of Product Reviews")


#Question 2
products_reviews_by_rating <- function(products_df, reviews_df, myrating){ 
    merge_results <- merge(products_df, reviews_df, by="key")
    products_reviews_results <- merge_results[merge_results$rating >= myrating, ]
    return(products_reviews_results)
}

#Question 3

#Defines the function products_reviews_by_rating that takes in 3 parameters: products_df, reviews_df and myrating
products_reviews_by_rating <- function(products_df, reviews_df, myrating){ 
    
    #merges products_df and reviews_df using the key column and puts the result into merge_results
    merge_results <- merge(products_df, reviews_df, by="key")
    
    #uses indexing to find the ratings in the merge_results df that are greater than or equal to myrating and stores 
    #them in products_reviews_results.
    products_reviews_results <- merge_results[merge_results$rating >= myrating, ]
    
    #returns the value(s) of products_reviews_results
    return(products_reviews_results)
}


#Question 4

my_selection <- products_reviews_by_rating(products, reviews, 4.5)
dim(my_selection)

#Question 5

numProducts <- function(x){
    hasIngredient <-trimws(unlist(strsplit(products$ingredients, ",|\\(|\\)")))
    num <- sum(hasIngredient==x) 
    return (num)
}
numProducts("SALT")