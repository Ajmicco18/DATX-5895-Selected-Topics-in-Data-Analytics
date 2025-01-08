#Question 1

options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
benfords_law <- function(d) log10(1+1/d)
digits <-1:9
bf_val<-benfords_law(digits)
plot(digits, bf_val, xlab = "digits", ylab="probabilities", main="Benfords Law Plot Line")



#Question 2

first_digit <- function(number){
    if (number!=0){
        
        number <- abs(number)
    
        while(number >= 10){
            number <- number/10
        }
    
        while(number < 1){
            number <-number*10
        }
        number<-floor(number)
    }
    return (number)
}
first_digit(0.0000546)
first_digit(-10239485)
first_digit(987654321)



#Question 3

library(data.table)
myDF <- fread("/anvil/projects/tdm/data/restaurant/orders.csv")
myDF$fd_grand_total <- sapply(myDF$grand_total,first_digit)
head(myDF$grand_total)
head(myDF$fd_grand_total) 



#Question 4

table(myDF$fd_grand_total)
plot(table(myDF$fd_grand_total)/length(myDF$fd_grand_total))



#Question 5

delivery <- function(start_date, end_date){
    orders_by_dates <- subset(myDF, ((myDF$delivery_date >= start_date) & (myDF$delivery_date <= end_date)))
    return(orders_by_dates)
}       
dim(myDF)
head(myDF$delivery_date)
resultDF <- delivery("2019-06-30","2019-07-31")
dim(resultDF)
resultDF <- delivery("2019-07-18","2019-08-02")
dim(resultDF)
resultDF <- delivery("2019-08-21","2019-08-22")
dim(resultDF)