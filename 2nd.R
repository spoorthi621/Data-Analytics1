#Boxplot
boxplot(Book1_csv$Salary,horizontal = TRUE)

#scatterplot3d
install.packages("scatterplot3d")
library(scatterplot3d)
attach(Book1_csv)
scatterplot3d(Salary,Start_Date,main="scatter_plot",xlab="salary",ylab = "start_date",zlab="dept",pch=18)

#scatterplot
attach(Book1_csv)
plot(Salary,Start_Date,main="scatter_plot",xlab="Salary",ylab = "Start_Date",pch=18)