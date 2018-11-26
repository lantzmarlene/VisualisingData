from matplotlib import pylab as plt
import pandas

df1 = pandas.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pandas.to_datetime(df1.Date)

df2 = pandas.read_excel("iphone-dates.xlsx")
print(df2)
df2['Date'] = pandas.to_datetime(df2.Date)
indexes = []
for date2 in df2.Date:
    for date1 in df1.Date:
        if date2 == date1:
            # print(date1)
            # print(df1.index[df1.Date == date1])
            indexes.append(df1.index[df1.Date == date1][0])

mean = df1["Close"].mean()
ax = df1.plot(x="Date", y="Close", style='r-', linewidth=0.6, label="Stock price, mean="+str(mean), title="Apple stock vs Iphone launch date", figsize=(18, 9))
df1.plot(x="Date", y="Close", style='-o', ms=7, markevery=indexes, linewidth=0, ax=ax, label="Iphone launch date")

# df1.set_index("Date").plot()

plt.show()