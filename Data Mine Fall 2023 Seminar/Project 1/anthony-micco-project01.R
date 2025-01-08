system("hostname", intern=TRUE)

#Calculate memory in bytes in Anvil sub-cluster A
256000*1000000000

#Calculate memory in TB in Anvil sub-cluster A
256000/1000

dat <- read.csv("/anvil/projects/tdm/data/disney/flight_of_passage.csv")
head(dat)
flight_of_passage <- dat
head(flight_of_passage)
rm(dat)
head(dat)