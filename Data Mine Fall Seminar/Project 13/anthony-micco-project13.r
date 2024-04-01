#Question 1
options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
library(data.table)
iceCreamDf<-fread("/anvil/projects/tdm/data/icecream/combined/products.csv")
ratingTotal<-tapply(iceCreamDf$rating_count, iceCreamDf$brand, sum)
barplot(ratingTotal, xlab="Ice Cream Brand", ylab="Sum of Ratings", main="Sum of Ratings for Each Brand", col="skyblue") 


#Question 2
mybrands <- c("bj", "breyers", "talenti")
myfiles <- paste0("/anvil/projects/tdm/data/icecream/", mybrands, "/reviews.csv")
bigDF <- do.call(rbind, lapply(myfiles, fread))
head(bigDF)
head(sort(table(format(bigDF$date, "%m-%Y")), decreasing=TRUE))
starsPerYear<-tapply(bigDF$stars, format(bigDF$date,"%Y"), mean)
barplot(starsPerYear, xlab="Year", ylab="Avg Number of Stars", main="Average Number of Stars Per Year")


#Question 3
tail(sort(tapply(bigDF$stars, bigDF$key, mean),decreasing=TRUE))
bigDF[nchar(bigDF$text)>2500]
dim(bigDF[nchar(bigDF$text)>2500])


#Question 4
head(sort(table(bigDF$author),decreasing=TRUE))
bigDF[(bigDF$author=="FuzzyGut") & (bigDF$stars==1)]
dim(bigDF[(bigDF$author=="FuzzyGut") & (bigDF$stars==1)])