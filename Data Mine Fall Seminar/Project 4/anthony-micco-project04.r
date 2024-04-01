Question 1
# code to list files
list.files("/anvil/projects/tdm/data/craigslist")

# code to read in files to myDF
myDF <- read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv", stringsAsFactors = TRUE)

#code to structure data
options(repr.matrix.max.cols=25, repr.matrix.max.rows=200)
options(jupyter.rich_display = F)

#code to find how many unique states
table(myDF$state)
length(table(myDF$state))

#code to find the most common states
sort((table(myDF$state)))

#code to find the number of cars that cost > $2000
sum(myDF$price[myDF$price>=2000])

#code to find the mean price of the cars
mean(myDF$price)


Question 2
# code to create mileage_category
myDF$mileage_category <- cut(myDF$odometer, breaks=c(0,50000,100000,150000,Inf), labels=c("Low", "Moderate","High","Very High"))
head(myDF$mileage_category)

# code to create has_VIN
dim(myDF)
myDF$has_VIN <- rep("does not have VIN", times=426880)
myDF$has_VIN[myDF$VIN != ""] <- "has vin"
dim(subset(myDF, VIN != ""))
dim(subset(myDF, myDF$has_VIN == "has vin"))

# code to create description_length
mynchar <- nchar(as.character(myDF$description))
myDF$description_length <-cut(mynchar, breaks=c(0,50,100,200,500,Inf),labels=c("Very Short", "Short", "Medium","Long","Very Long"))
head(myDF$description_length)


Question 3
# code to get the number of cars in each mileage category
table(myDF$mileage_category)

# code to get the number of cars with and without VIN numbers
table(myDF$has_VIN)

# code to get the number of cars in each description category
table(myDF$description_length)


Question 4
# code to create myTexasDF
dim(myDF)
myTexasDF <- subset(myDF, state=="tx")
dim(myTexasDF)
head(myTexasDF)

# code to find the most popular state
sort(table(myDF$state))

# code to make popularStateDF
popularStateDF <- subset(myDF, state=="ca")
dim(popularStateDF)
head(popularStateDF)

# code to create myFavoriteDF 
myFavoriteDF <- subset(myDF, state=="oh")
dim(myFavoriteDF)
head(myFavoriteDF)


Question 5
#Map 1
options(jupyter.rich_display=T)
myDF<-read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv",stringsAsFactors=TRUE)
myTexasDF<-subset(myDF, state=="tx" & !is.na(lat) & !is.na(long))
library(leaflet)
library(sf)
points <- st_as_sf(myTexasDF, coords=c("long","lat"),crs=4326)
addCircleMarkers(addTiles(leaflet(myTexasDF)),radius=1)


#Map 2
options(jupyter.rich_display=T)
myDF<-read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv",stringsAsFactors=TRUE)
popularStateDF<-subset(myDF, state=="ca" & !is.na(lat) & !is.na(long))
library(leaflet)
library(sf)
points <- st_as_sf(popularStateDF, coords=c("long","lat"),crs=4326)
addCircleMarkers(addTiles(leaflet(popularStateDF)),radius=1)


#Map 3
options(jupyter.rich_display=T)
myDF<-read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv",stringsAsFactors=TRUE)
myFavoriteDF<-subset(myDF, state=="oh" & !is.na(lat) & !is.na(long))
library(leaflet)
library(sf)
points <- st_as_sf(myFavoriteDF, coords=c("long","lat"),crs=4326)
addCircleMarkers(addTiles(leaflet(myFavoriteDF)),radius=1)