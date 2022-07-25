#Mean
mean = mean(book2$Total)
print(mean)

#Median
median = median(book2$Total)
print(median)

#Mode
install.packages("modeest")
library(modeest)
mlv(book2$Total,method="mfv")

#Percentile
d<-c(14,12,19,23,5,13,28,17)
print(d)
quantile(d,c(0.30))


#MinMax
min(d)
max(d)

#Range
range(d)
print(max(d)-min(d))

#Variance
var(book2$Total)

#Quantile
a<-c(8,1,23,9,4)
q1<-quantile(a,c(0.25))
print(q1)

q2<-quantile(a,c(0.50))
print(q2)

q3<-quantile(a,c(0.75))
print(q3)

#InterQuantile
IQR(a)

#SD
sd(book2$Total)

#Population SD
sd(book2$Total)*sqrt((79-1)/79)

#BoxPlot
boxplot(book2$Total,horizontal = TRUE)

#Skew
skewness(book2$Total)
