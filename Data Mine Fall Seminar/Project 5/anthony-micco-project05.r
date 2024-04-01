#Question 1

# read in csv file and create data frame
options(jupyter.rich_display = F)
myDF <- read.csv("/anvil/projects/tdm/data/election/escaped2020sample.txt", sep="|")
options(repr.matrix.max.cols=30, repr.matrix.max.rows=200)
head(myDF)
# separates the date values in TRANSACTION_DT and creates new column called newdates
library(lubridate, warn.conflicts = FALSE)
myDF$newdates <-mdy(myDF$TRANSACTION_DT)
# create new column TRANSACTION_YR
library(lubridate, warn.conflicts = FALSE)
myDF$TRANSACTION_YR <-year(myDF$newdates)
head(myDF$TRANSACTION_YR)
# find the sum of the values in TRANSACTION_AMT grouped by TRANSACTION_YR
tapply(myDF$TRANSACTION_AMT, myDF$TRANSACTION_YR, sum)
# plotting the amount of transcations 
plot(myDF$TRANSACTION_YR,myDF$TRANSACTION_AMT, xlab="Year",ylab="Amount of Transactions")


#Question 2

# creates the 2020 date frame
my2020DF <- subset(myDF, TRANSACTION_YR == "2020")
head(my2020DF)
# sum of the transactions in each month of 2020
my2020DF$month <-month(my2020DF$newdates)
tapply(my2020DF$TRANSACTION_AMT,my2020DF$month,sum)
#plot the data
plot(my2020DF$month,my2020DF$TRANSACTION_AMT, xlab="Month",ylab="Amount of Transactions")


#Question 3

# finding the donor who gave the most money
tail(sort(tapply(myDF$TRANSACTION_AMT, myDF$NAME, sum)))
# finding the total amount of money given by each state
tapply(myDF$TRANSACTION_AMT,myDF$STATE,sum)
# sorting the states based on how much money they gave
sort(tapply(myDF$TRANSACTION_AMT,myDF$STATE,sum))
#finding the ten zipcodes that donated the most money
tail(sort(tapply(myDF$TRANSACTION_AMT,myDF$ZIP_CODE,sum)),10)


#Question 4
# using a barplot to plot the total amount of money in the top 5 states
top_states <- tail(sort(tapply(myDF$TRANSACTION_AMT,myDF$STATE,sum)),5)
barplot(top_states, main="States Donating the Most Money",xlab="State",ylab="Transaction Amount", col="black")
# using a dotplot to plot the total amount of money in the top 10 zipcodes
top_zip_code <- tail(sort(tapply(myDF$TRANSACTION_AMT,myDF$ZIP_CODE,sum)),10)
dotchart(top_zip_code, main="Zip Codes Donating the Most Money",xlab="Transaction Amount",ylab="Zip Code", col="black")


#Question 5
top_occupation_donors <- tail(sort(tapply(myDF$TRANSACTION_AMT, myDF$OCCUPATION, sum)),10)
dotchart(top_occupation_donors, main="Occupations that Donated the Most Money",ylab="Occupation",xlab="Transaction Amount",col="black")