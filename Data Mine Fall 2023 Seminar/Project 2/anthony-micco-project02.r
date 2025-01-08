#Code to read in .csv file
myDF <- read.csv("/anvil/projects/tdm/data/flights/subset/1995.csv")

#Code to get the head of myDF
head(myDF)

#Code to get the dimensions of the data frame
dim(myDF)

#Code to get the date type for each variable in the data frame
str(myDF)

#code to create new vector
my_airports <- myDF$Origin

#code to get the date type of the my_airports vector
class(my_airports)

#code to get the first 250 entries
head(my_airports,250)

#code to see flights departing Indy
str(myDF$Origin[myDF$Origin=="IND"])

#code to see flights arriving in Indy
str(myDF$Dest[myDF$Dest=="IND"])

# code to get data from row 894
myDF[894,]$Origin
myDF[894,]$Dest

# code to get distances less than 200 miles
str(myDF$Distance[myDF$Distance < 200])

# code to order airline companies
sort(table(myDF$UniqueCarrier))

#Code to get the planes with the greatest number of flights 
tail(sort(table(myDF$TailNum)),10)

# code to create histogram
hist(myDF$Distance,main="Flight Distances", xlab="Distance",ylab="Frequency")