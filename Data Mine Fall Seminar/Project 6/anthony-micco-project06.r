options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
myDF <- read.csv("/anvil/projects/tdm/data/olympics/athlete_events.csv", stringsAsFactors=TRUE)
head(myDF)

#Question 1
#Making a table to list all the games in DF
table(myDF$Games)

#Getting the countries that participated in the 1980 games
my1980athletes <- table(myDF$NOC[myDF$Year == 1980])
my1980athletes[my1980athletes != 0]

#Gathering the data to find the names of athletes attending multiple games
myDuplicatedAthletes <- unique(myDF$Name[duplicated(myDF$Name)])
myNewDF <- subset(myDF, Name %in% myDuplicatedAthletes)
head(myNewDF)


#Question 2
# finding average age of athletes 
tapply(myDF$Age, myDF$NOC, mean)

#Finding the max height by sport and sorting the max heights
head(sort(tapply(myDF$Height, myDF$Sport, max, na.rm=TRUE), decreasing= TRUE),5)


#Question 3 
# Getting the number of rows in data frame
dim(myDF)

#changing the MonthOfDeath column from numbers to month
table(myDF$MonthOfDeath)
month_order <- c("January","February","March","April","May","June","July","August","September","October","November","December")
myDF$MonthOfDeath <- factor(myDF$MonthOfDeath)
levels(myDF$MonthOfDeath) <- month_order
head(myDF$MonthOfDeath)

#totaling the number of people to die in each month
table(myDF$MonthOfDeath)


#Question 4
# finding the average age for each race at the time of death
sort(tapply(myDF$Age, myDF$Race, mean),decreasing=TRUE)

#finding the average age for females of each race at the time of death
sort(tapply(myDF$Age[myDF$Sex == "F"], myDF$Race[myDF$Sex=="F"], mean),decreasing=TRUE)

#finding the average age for males of each race at the time of death
sort(tapply(myDF$Age[myDF$Sex == "M"], myDF$Race[myDF$Sex=="M"], mean),decreasing=TRUE)


#Question 5
# code creating graph about Olympic data frame
myOlympicDF <- read.csv("/anvil/projects/tdm/data/olympics/athlete_events.csv", stringsAsFactors=TRUE)
my2016DF <- subset(myOlympicDF, myOlympicDF$Year == 2016)
myOlympicWeights <- tail(sort(tapply(my2016DF$Weight, my2016DF$NOC, mean,na.rm=TRUE)),5)
barplot(myOlympicWeights, main="Highest Average Weight of Athletes: 2016 Olympics",xlab="Country",ylab="Weight (KG)",col="blue") 

# code creating graph about death record data frame
myDeathRecordDF <- read.csv("/anvil/projects/tdm/data/death_records/DeathRecords.csv", stringsAsFactors = TRUE)
maritalStatus <- sort(table(myDeathRecordDF$MaritalStatus))
dotchart(maritalStatus,main="Number of Deaths by Marital Status", ylab="Marital Status",xlab="Number",col="black")

