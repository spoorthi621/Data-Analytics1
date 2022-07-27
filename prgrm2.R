#outliers
install.packages("outliers")
library(outliers)
test <- grubbs.test(book2$Total)
test

#histogram
hist(Salary,xlab="Salary",col="maroon",border="black")

