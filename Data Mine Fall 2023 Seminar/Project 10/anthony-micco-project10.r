#Question 1
options(jupyter.rich_display = F)
options(repr.matrix.max.cols = 25, repr.matrix.max.rows =200)
library(data.table)
orders <- fread("/anvil/projects/tdm/data/restaurant/orders.csv")
vendors <-fread("/anvil/projects/tdm/data/restaurant/vendors.csv")

fryDF <- subset(vendors, grepl("Fries",vendor_tag_name))
fryDF_ <- vendors[grep("Fries",vendors$vendor_tag_name),]

dim(fryDF)
dim(fryDF)



#Question 2
table(vendors$delivery_charge)
prop.table(table(vendors$delivery_charge))



#Question 3
table(vendors$delivery_charge[vendors$vendor_category_id==2])
prop.table(table(vendors$delivery_charge[vendors$vendor_category_id==2]))

table(vendors$delivery_charge[vendors$vendor_category_id==3])
prop.table(table(vendors$delivery_charge[vendors$vendor_category_id==3]))



#Question 4
tapply(vendors$delivery_charge, vendors$vendor_category_id, table)

tapply(vendors$delivery_charge, vendors$vendor_category_id, function(x){prop.table(table(x))})


#Question 5
sapply(tapply(vendors$delivery_charge, vendors$vendor_category_id, table),prop.table, simplify=FALSE)