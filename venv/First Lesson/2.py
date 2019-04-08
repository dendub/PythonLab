import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import interp
import matplotlib.ticker as ticker
def first():
    filename = "scatter.txt"
    file = open(filename, "r")
    tmp = []
    x = []
    y = []

    for line in file:
        tmp.append(line)

    for word in tmp[0].split():
        x.append(float(word))

    for word in tmp[1].split():
        y.append(float(word))
    file.close

    plt.axes(polar=True)

    data = []
    for num in y:
        data.append((num+5)*20)

    clr = cm.copper(data)

    plt.scatter(x, y, 10, y)
    plt.show()

def second():
    filename = "bars.txt"
    file = open(filename, "r")
    tmp = []
    for line in file:
        tmp.append(line)

    x = [float(i) for i in tmp[0].split()]
    y = [float(i) for i in tmp[1].split()]

    for cx, cy in zip(x, y):
        plt.bar(cx, cy, 0.5, color=[cy, 0, cy, 1])
    plt.show()

def third():
    filename = "pie.txt"
    file = open(filename, "r")

    x = [float(i) for i in file.readline().split()]

    plt.pie(x, explode=[0.2, 0.03, 0.03, 0.03, 0.03])
    plt.show()

def fourth():
    filename = "data2.dat"
    file = open(filename, "r")

    x = [float(line) for line in file]
    print(x)

    plt.subplot(122)
    plt.hist(x, density=1, histtype='step', cumulative=True)
    plt.subplot(121)
    plt.hist(x, histtype='step')

    plt.show()


def fifth():
    filename = "data3.dat"
    file = open(filename, "r")

    x = [[float(i) for i in line.split(',')] for line in file]

    plt.boxplot(x)
    plt.show()



def sixth():
    x=[0,1,2,3,4]
    y=[0,2.3,2.7,2.9,3]
    fig,ax = plt.subplots(1, figsize=(7,5))
    ax.plot(x, y, linestyle="-.", marker="o", color="red", markerfacecolor='blue', markersize=10 )
    plt.xlim(0,4)
    plt.xticks([0,0.5,1,1.5,2,2.5,3,3.5,4])

    plt.ylim(0,3)
    plt.yticks([0,0.5,1,1.5,2,2.5,3])
    plt.grid(which='major', color='#666666')
    plt.minorticks_on()
    plt.grid(which='minor', color='#999999')
    plt.tick_params(labelbottom=False)
    plt.tick_params(labelleft=False)

    plt.show()
sixth()

def seventh():
    x=[0,1,2,3,4]
    y=[0,2.3,2.7,2.8,3]
    ax = plt.gca()

    ax.xaxis.set_major_locator((ticker.NullLocator()))
    ax.yaxis.set_major_locator((ticker.NullLocator()))
    ax.plot(x, y, linestyle="-.", marker="o", color="red", markerfacecolor='blue', markersize=10)

    plt.show()

#seventh()

#fifth()
#fourth()
#third()



#second()

#first()