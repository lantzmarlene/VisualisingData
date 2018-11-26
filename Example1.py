from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []
series4 = []

for i in range(0,30):
    series1.append(i)
    series2 += [i*i]
    series3 += [i**3]
    series4.append(1.5**i)

plt.figure("first")
plt.plot(list(range(0,30)), series1, "r+", label="Linear", linewidth=2, ms=10)
#plt.figure("second")
plt.plot(list(range(0, 30)), series2, "k^:", label="Quadratic", linewidth=0.5)
plt.legend(loc = "upper left")
plt.figure("third")
plt.plot(list(range(0, 30)), series3)
plt.figure("fourth")
plt.plot(list(range(0, 30)), series4)

plt.figure("first")
plt.title("Linear")
plt.ylim(0,1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.figure("second")
plt.title("Quadratic")

plt.figure("third")
plt.title("Cubic")
plt.ylabel("Cubic Progression")
plt.figure("fourth")
plt.show()