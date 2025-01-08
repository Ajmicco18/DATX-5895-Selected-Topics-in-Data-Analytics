#Question 1
options(jupyter.rich_display=F)
options(repr.matrix.max.cols=30,repr.matrix.max.rows=200)
library(data.table)
orders<-fread("/anvil/projects/tdm/data/restaurant/orders.csv")
sort(table(year(orders$created_at)),decreasing=TRUE)
table(wday(orders$created_at))
plot(table(wday(orders$created_at)),type="l", xlab="Day of the week",ylab="Avg number of orders", main="Avg number of orders per day") 


#Question 2

head(orders$vendor_id[year(orders$created_at)==2019])
head(orders$vendor_id[year(orders$created_at)==2020])
tapply(orders$vendor_id, year(orders$created_at), function(x){head(sort(table(x),decreasing=TRUE))})
df19<-subset(orders, year(created_at)==2019)
df20<-subset(orders, year(created_at)==2020)
tapply(df19$grand_total, df19$vendor_id,function(x){head(sort(sum(x),decreasing=TRUE))})
tapply(df20$grand_total, df20$vendor_id,function(x){head(sort(sum(x),decreasing=TRUE))})


#Question 3

head(orders$created_at)
hour(head(orders$created_at))
tail(orders$created_at)
hour(tail(orders$created_at))
sum(sort(table(hour(orders$created_at[(hour(orders$created_at)>17)])),decreasing=TRUE))
sum(sort(table(hour(orders$created_at[(hour(orders$created_at)<17)])),decreasing=TRUE))
beforeFive<-table(wday(orders$created_at[hour(orders$created_at)<17]))
afterFive<-table(wday(orders$created_at[hour(orders$created_at)>17]))
myDF<-data.frame(group=c(rep("Before Five",times=7),rep("After Five",times=7)),TotalOrders=c(beforeFive,afterFive),DaysOfWeek=c(1:7,1:7))
library(ggplot2)
ggplot(myDF, aes(DaysOfWeek, TotalOrders, fill=group)) + geom_col(position = "dodge")


#Question 4

head(orders)
itemTotal<-tapply(orders$grand_total, orders$item_count, sum)
barplot(itemTotal,xlab="Number of Items",ylab="Total Cost", main="Total Cost of Purchase with X Items") 

tapply(year(orders$created_at), orders$payment_mode, table)
pay19<-table(orders$payment_mode[year(orders$created_at)==2019])
pay20<-table(orders$payment_mode[year(orders$created_at)==2020])
paymentDF<-myDF<-data.frame(group=c(rep("2019",times=5),rep("2020",times=5)),TotalOrders=c(pay19,pay20),PaymentMethod=c(1:5,1:5))
ggplot(paymentDF, aes(PaymentMethod, TotalOrders, fill=group)) + geom_col(position = "dodge")

totalOrdersPerMonth<-tapply(orders$vendor_id, month(orders$created_at),sum)
barplot(totalOrdersPerMonth,xlab="Month", ylab="Total Orders", main="Total Number of Orders Per Month")