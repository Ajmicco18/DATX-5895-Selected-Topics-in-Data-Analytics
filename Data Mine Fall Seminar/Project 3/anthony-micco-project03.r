# code to read files 
list.files("/anvil/projects/tdm/data/craigslist")
file.info("/anvil/projects/tdm/data/craigslist/vehicles.csv")$size

# code to create data frame
myDF <- read.csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")

# code to get the number of rows and columns
dim(myDF)

#code to get the data types 
str(myDF)

# code to get the number of number of NA values 
sum(is.na(myDF$year))
dim(myDF)[1]

# code to get percentage 
sum(is.na(myDF$year)) / dim(myDF)[1]

# Creating the goodyearsDF
goodyearsDF <- subset(myDF, !is.na(year))
head(goodyearsDF)

#code to create missingyearsDF
missingyearsDF <- subset(myDF, is.na(year))
head(missingyearsDF)

# code to find the mean price of vehicles
subset(aggregate(price ~ year, data= myDF, FUN=mean), year>2002)

#code to find the most frequent year 
which.max(table(myDF$year))

# code to find the most popular region_url
tail(sort(table(myDF$region_url)))

# code to find the most popular three states
tail(sort(table(myDF$state)))

# code to create a scatter plot of means from the year 2003-2022
myyears <-subset(aggregate(price ~ year, data= myDF, FUN=mean), year>2002)$year
myprice <-subset(aggregate(price ~ year, data= myDF, FUN=mean), year>2002)$price
plot(myyears[myprice<50000], myprice[myprice<50000], xlab="Year",ylab="Price ($)")

# code to create a line plot of means from the year 2003-2022
myyears <-subset(aggregate(price ~ year, data= myDF, FUN=mean), year>2002)$year
myprice <-subset(aggregate(price ~ year, data= myDF, FUN=mean), year>2002)$price
plot(myyears[myprice<50000], myprice[myprice<50000], type="l", xlab="Year",ylab="Price ($)")
