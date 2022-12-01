import matplotlib.pyplot as plt

x = []
y = []
px = 1/plt.rcParams['figure.dpi']


with open("DS1.txt") as f:
    coordinates = f.readline()

    while coordinates:
        x.append(int((coordinates.split()[0])))
        y.append(int(coordinates.split()[1]))
        coordinates = f.readline()


plt.figure(figsize=(960*px, 540*px))

plt.scatter(x, y)
plt.axis("off")
plt.savefig("data_set_plot.png")




