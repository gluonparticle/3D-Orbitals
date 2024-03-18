import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('/home/gluonparticle/HiggsField/QuantumVacuumFluctuations/quantum.csv')


print("""Type 0 for ONLY Radial
Type 1 for ONLY Angular
Type 2 for DUAL (Radial*Angular)""")


print()
print()

x1=int(input("Type the appropriate number:"))

print()
print()

if x1!=0:
    print("     NUMBER     TYPE_OF_ORBITAL")      
    print('''     1         4f(x3)
     2         4f(y3)
     3         4f(z3)
     4         4f(yz2)
     5         4f(xz2)
     6         4f(xyz)
     7       4f(y(3x2-y2))
     8       4f(x(x2-3y2))
     9       4f(x(z2-y2))
     10      4f(y(z2-x2))
     11      4f(z(x2-y2))''')
    print()
    print()
    x2=int(input("Please find the appropriate number for your 4f-orbital type:"))


    
    
    



#Defining a Multivariable function for probability Distribution
def prob(x,y,z):
    r=np.sqrt(np.square(x)+np.square(y)+np.square(z))

    if x1!=0:
        
        if x2==1:
            A_Variable=x*(5*x**2 - 3*r**2)/(r+0.000000000001)**3
                
        elif x2==2:
            A_Variable=y*(5*y**2 - 3*r**2)/(r+0.000000000001)**3
       
        elif x2==3:
            A_Variable=z*(5*z**2 - 3*r**2)/(r+0.000000000001)**3
     
        elif x2==4:
            A_Variable=y*(5*z**2 - r**2)/(r+0.000000000001)**3

        elif x2==5:
            A_Variable=x*(5*z**2 - 3*r**2)/(r+0.000000000001)**3
      
        elif x2==6:
            A_Variable=2*x*y*z/(r+0.000000000001)**3
    
        elif x2==7:
            A_Variable=y*(3*x**2 - y**2)/(r+0.000000000001)**3
    
        elif x2==8:
            A_Variable=x*(x**2 - 3*y**2)/(r+0.000000000001)**3
    
        elif x2==9:
            A_Variable=x*(z**2 - y**2)/(r+0.000000000001)**3
   
        elif x2==10:
            A_Variable=y*(z**2 - x**2)/(r+0.000000000001)**3

        elif x2==11:
            A_Variable=z*(x**2 - y**2)/(r+0.000000000001)**3

        else:
            print("Please select appropriate number and try again")



    rho=df.iloc[0,5]*r



    if x1==0:
        Radial  =  np.exp(-0.5*rho) * df.iloc[0,5]
        Angular=1

    elif x1==1:
        Radial  =  1
        Angular =  A_Variable       * df.iloc[x2,4]

    elif x1==2:
        Radial  =  np.exp(-0.5*rho) * df.iloc[0,5]
        Angular =  A_Variable       * df.iloc[x2,4]
        
    else:
        print("Please select the appropriate number and try again")
        
        
    Wavefunction=Radial*Angular
    return np.square(Wavefunction)



#Assigning Random coordinates
x=np.linspace(0,1,100)
y=np.linspace(0,1,100)
z=np.linspace(0,1,100)

elements = []
probability = []

for ix in x:
    for iy in y:
        for iz in z:
            
            #Serialize into 1D object
            elements.append(str((ix,iy,iz)))
            probability.append(prob(ix,iy,iz))
            
#Ensure sum of probability is 1
probability = probability/sum(probability)

#Getting electron coordinates based on probabiliy
coord = np.random.choice(elements, size=40000, replace=True, p=probability)
elem_mat = [i.split(',') for i in coord]
elem_mat = np.matrix(elem_mat)



x_coords = [float(i.item()[1:]) for i in elem_mat[:,0]]
y_coords = [float(i.item()) for i in elem_mat[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in elem_mat[:,2]]

#Plotting the figure based on coordinates retrieved from the matrix
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')




from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(fig)
ax.scatter(x_coords, y_coords, z_coords, alpha=0.4, s=2)

if x2 in range(0,4):
    i=25
elif x2 in range(4,7):
    i=-25

elif x2 in range(7,9):
    i=-140

elif x2 in range(9,12):
    i=-40

ax.view_init(azim=i, elev=15)


fig.add_axes(ax)
plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
plt.show()
plt.savefig("NEW.jpeg")

