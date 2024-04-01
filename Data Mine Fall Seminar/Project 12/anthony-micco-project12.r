#Question 1

options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
library(data.table)
orders<-fread("/anvil/projects/tdm/data/restaurant/orders.csv")
head(orders)
head(orders$created_at)
sort(table(substr(orders$created_at,1,7)),decreasing=TRUE)
sort(table(paste(year(orders$created_at),month(orders$created_at))),decreasing=TRUE)
sort(table(format(orders$created_at,"%Y-%m")),decreasing=TRUE)


#Question 2

head(sort(table(orders$customer_id),decreasing=TRUE))
sort(table(format(orders$created_at[orders$customer_id=="XW90EAP"],"%Y-%m")),decreasing=TRUE)


#Question 3

sort(table(orders$payment_mode),decreasing=TRUE)
sort(table(orders$payment_mode[orders$customer_id=="XW90EAP"]),decreasing=TRUE)


#Question 4

ordersJan2020<-subset(orders, (year(created_at)==2020)&(month(created_at)==1))
monthlySum<-tapply(ordersJan2020$grand_total, wday(ordersJan2020$created_at), sum)
barplot(monthlySum, xlab="Day of Week", ylab="Sum of Grand Total", main="Sum of Grand Totals Per Day of Week in Jan 2020")