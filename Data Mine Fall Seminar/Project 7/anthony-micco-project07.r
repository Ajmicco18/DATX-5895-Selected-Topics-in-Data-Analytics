#Question 1
options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
library(data.table)
products <- fread("/anvil/projects/tdm/data/icecream/combined/products.csv")
reviews <- fread("/anvil/projects/tdm/data/icecream/combined/reviews.csv")
titles <- fread("/anvil/projects/tdm/data/movies_and_tv/titles.csv")
episodes <- fread("/anvil/projects/tdm/data/movies_and_tv/episodes.csv")
ratings <- fread("/anvil/projects/tdm/data/movies_and_tv/ratings.csv")
head(products$ingredients, n=1)
GuarGumDF <- subset(products, grepl("GUAR GUM", ingredients))
sort(GuarGumDF$rating,decreasing=TRUE)


#Question 2
names(products)
names(reviews)
class(products$ingredients)
class(reviews$ingredients)
newDF <- merge(products,reviews, by=c("brand","key"))
dim(newDF)


#Question 3
head(episodes)
StrangerThings <- subset(episodes,show_title_id=="tt4574334")
head(titles)
head(StrangerThings)
head(ratings)
BigStrangerThingsDF <- merge(merge(merge(merge(StrangerThings, titles, by.x="show_title_id",by.y="title_id"),
                                  titles, by.x="episode_title_id", by.y="title_id"),
                                  ratings, by.x="show_title_id", by.y="title_id"),
                                  ratings, by.x="episode_title_id", by.y="title_id")
names(BigStrangerThingsDF)
names(BigStrangerThingsDF)[6] <- "show_title"
names(BigStrangerThingsDF)[14] <- "episode_title"
names(BigStrangerThingsDF)[21] <- "show_rating"
names(BigStrangerThingsDF)[23] <- "episode_rating"
head(BigStrangerThingsDF[order(BigStrangerThingsDF$episode_rating, decreasing=TRUE),],n=5)


#Question 4
BigStrangerThingsDF[(BigStrangerThingsDF$season_number==3)&(BigStrangerThingsDF$episode_rating < 8.5)]
Season3DF <- subset(BigStrangerThingsDF, (season_number==3)&(episode_rating < 8.5))
dim(BigStrangerThingsDF[(BigStrangerThingsDF$season_number==3)&(BigStrangerThingsDF$episode_rating < 8.5)])
dim(Season3DF)


#Question 5
season_number <- 3
subset(BigStrangerThingsDF, (season_number == season_number) & (episode_rating < 8.5))