from matplotlib import pylab as plt
import pandas
import datetime

df1 = pandas.read_csv("C:/Users/Marlene Lantz/Downloads/Nikon.csv")
print("Nikon: ")
print(df1.head())
df1['Date'] = pandas.to_datetime(df1.Date)


df2 = pandas.read_csv("C:/Users/Marlene Lantz/Downloads/Canon.csv")
print("Canon: ")
print(df2.head())
df2['Date'] = pandas.to_datetime(df2.Date)


plt.figure("High Stock")
plt.plot(df1.Date, df1.High, "r-", df2.Date, df2.High, "b-", linewidth=0.6, label="Canon Stock Price")
plt.show()