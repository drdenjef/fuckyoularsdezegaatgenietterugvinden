import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


Dimensions = 2

aanvulling = "x_RK4"

bestand = "{}.txt".format(aanvulling)
posities = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)
N = int(len(posities)/3)

plt.rc('axes', axisbelow=True)   # zet de grid op de achtergrond

if Dimensions == 2:    
    plt.figure(figsize=(6, 6))
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    if "burrau" in aanvulling:
        plt.xlim(-4.5, 4.5)
        plt.ylim(-4.5, 4.5)
        plt.scatter(1, 3, c = 'black')
        plt.scatter(1, -1, c = 'black')
        plt.scatter(-2, -1, c = 'black')
    
    x1 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[0]
    y1 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[1]
    plt.plot(x1, y1, c = 'orange', label = 'Deeltje 1')
    
    x2 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[3]
    y2 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[4]
    plt.plot(x2, y2, c = 'magenta', label = 'Deeltje 2')
    
    if N >= 3:
        x3 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[6]
        y3 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[7]
        plt.plot(x3, y3, c = 'cyan', label = 'Deeltje 3')
        
    if N >= 4:
        x4 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[9]
        y4 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[10]
        plt.plot(x4, y4, c = 'black', label = 'Deeltje 4')
    
    if N >= 5:
        x5 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[12]
        y5 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[13]
        plt.plot(x5, y5, c = 'blue', label = 'Deeltje 5')
    
    if N >= 6:
        x6 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[15]
        y6 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[16]
        plt.plot(x6, y6, c = 'yellow', label = 'Deeltje 6')
    
    if N >= 7:
        x7 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[18]
        y7 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[19]
        plt.plot(x7, y7, c = 'red', label = 'Deeltje 7')
        
else:
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.set_zlim(-4,4)
    
    x1 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[0]
    y1 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[1]
    z1 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[2]
    ax.scatter(x1, y1, z1, c = 'orange', label = 'Deeltje 1', marker = '.', linewidths=0.1)
    
    x2 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[3]
    y2 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[4]
    z2 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[5]
    ax.scatter(x2, y2, z2, c = 'magenta', label = 'Deeltje 2', marker = '.', linewidths=0.1)
    
    if N >= 3:
        x3 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[6]
        y3 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[7]
        z3 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[8]
        ax.scatter(x3, y3, z3, c = 'cyan', label = 'Deeltje 3', marker = '.', linewidths=0.1)
        
    if N >= 4:
        x4 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[9]
        y4 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[10]
        z4 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[11]
        ax.scatter(x4, y4, z4, c = 'black', label = 'Deeltje 4', marker = '.', linewidths=0.1)
    
    if N >= 5:
        x5 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[12]
        y5 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[13]
        z5 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[14]
        ax.scatter(x5, y5, z5, c = 'blue', label = 'Deeltje 5', marker = '.', linewidths=0.1)
    
    if N >= 6:
        x6 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[15]
        y6 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[16]
        z6 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[17]
        ax.scatter(x6, y6, z6, c = 'yellow', label = 'Deeltje 6', marker = '.', linewidths=0.1)
    
    if N >= 7:
        x7 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[18]
        y7 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[19]
        z7 = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)[20]
        ax.scatter(x7, y7, z7, c = 'red', label = 'Deeltje 7', marker = '.', linewidths=0.1)
    
plt.legend()
plt.show()





bestand = "{}_E_err.txt".format(aanvulling)
x_err, afstand, verstreken_tijd = np.loadtxt("C:\\Users\\Joren\\source\\repos\\AS_Project\\AS_Project\\" + bestand, unpack=True)

plt.figure()

plt.subplot(211)
plt.plot(verstreken_tijd, x_err, color = 'steelblue')
plt.xlabel("Tijd")
plt.ylabel(r"$\Delta$ Energie")
plt.grid()
plt.yscale('log')


plt.subplot(212)
plt.plot(verstreken_tijd, afstand, color = 'steelblue')
plt.gca().invert_yaxis()
plt.xlabel("Tijd")
plt.ylabel("Dichtste nadering")
plt.grid()

plt.show()



