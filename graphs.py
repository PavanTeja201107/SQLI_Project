import matplotlib.pyplot as plt

methods=["PVT","Structure","Parameterized","Hybrid"]

detection=[0.85,0.92,1.0,0.98]

recall=[0.80,0.90,1.0,0.96]

runtime=[0.01,0.04,0.02,0.05]

plt.figure()

plt.bar(methods,detection)

plt.title("Detection Rate")

plt.ylabel("Rate")

plt.show()


plt.figure()

plt.bar(methods,recall)

plt.title("Recall Comparison")

plt.ylabel("Recall")

plt.show()


plt.figure()

plt.bar(methods,runtime)

plt.title("Runtime Comparison")

plt.ylabel("Seconds")

plt.show()