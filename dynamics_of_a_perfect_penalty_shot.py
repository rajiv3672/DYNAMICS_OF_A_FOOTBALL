import matplotlib.pyplot as plt
import numpy as np

h = 0.0001#The step size
B1 = 0.0776#(rho * A)/2m
B2 = 2.2#B2 = spin angular velocity of the football \times Radius of the football, hence parameter for spin angular velocity
kl = 0.005998
g = 9.8

#Calculates the modulus of the velocity
def modv(x2, y2, z2):
    return np.sqrt(x2*x2 + y2*y2 + z2*z2)
#calculates the modulus of the velocity veectors projection in xy plane
def modvxy(x2, y2):
    return np.sqrt(x2*x2 + y2*y2)

#next 3 funcs are for solving the equations
def fx(x2, y2, z2):
    xret1 = -B1*x2*(0.8*B2 + 0.12*modv(x2, y2, z2))
    xret2 = kl*x2*z2*(modv(x2, y2, z2)/modvxy(x2, y2))
    xret3 = ((B1*y2)/modvxy(x2, y2))*(0.77*B2*modv(x2, y2, z2) + 0.12*(modv(x2, y2, z2)*modv(x2, y2, z2)))
    return (xret1 + xret2 + xret3)

def fy(x2, y2, z2):
    yret1 = -B1*y2*(0.8*B2 + 0.12*modv(x2, y2, z2))
    yret2 = kl*y2*z2*(modv(x2, y2, z2)/modvxy(x2, y2))
    yret3 = -((B1*x2)/modvxy(x2, y2))*(0.77*B2*modv(x2, y2, z2) + 0.12*(modv(x2, y2, z2)*modv(x2, y2, z2)))
    return (yret1 + yret2 + yret3)

def fz(x2, y2, z2):
    zret1 = -g
    zret2 = -B1*z2*(0.8*B2 + 0.12*modv(x2, y2, z2))
    zret3 = -kl*modv(x2, y2, z2)*modvxy(x2, y2)
    return (zret1 + zret2 + zret3)

Cd0 = 0.25
Cs0 = 0.264

#These next three functions are used instead of fx,fy,fz when spin ratio,Sp>0.3 
def fxa(x2, y2, z2):
    xret1 = -B1*Cd0*modv(x2, y2, z2)*x2
    xret2 = kl*(modv(x2, y2, z2)/modvxy(x2, y2))
    xret3 = B1*Cs0*((modv(x2, y2, z2)*modv(x2, y2, z2))/modvxy(x2, y2))*y2
    return (xret1 + xret2 + xret3)

def fya(x2, y2, z2):
    xret1 = -B1*Cd0*modv(x2, y2, z2)*y2
    xret2 = kl*(modv(x2, y2, z2)/modvxy(x2, y2))*x2*z2
    xret3 = -B1*Cs0*((modv(x2, y2, z2)*modv(x2, y2, z2))/modvxy(x2, y2))*x2
    return (xret1 + xret2 + xret3)

def fza(x2, y2, z2):
    zret1 = -g
    zret2 = -B1*Cd0*z2*modv(x2, y2, z2)
    zret3 = -kl*modv(x2, y2, z2)*modvxy(x2, y2)
    return (zret1 + zret2 + zret3)

#Intial velocities, I encourage you to change this.
X20=[2.7,2.3,2.5,3.1,3.2]
Y20=[14.64,22,22,18,25]
Z20=[7.8,7.8,7.6,7.9,8.4]

#when B2 rises by 1.1 so that the spin angular velocity rises by 10rad per sec
while(B2<=5.5):
    lum=0#a flag for counting
    while lum<5:
        #Loading initial conditions
        x20 = X20[lum]
        y20 = Y20[lum]
        z20 = Z20[lum]
        #Dynamic velocity's componets
        x2 = x20
        y2 = y20
        z2 = z20
        #Matrix for velocity's componets
        X2 = []
        Y2 = []
        Z2 = []

        #Initial position
        x10 = 0
        y10 = 0
        z10 = 0

        #Dynamic posittion
        x1 = x10
        y1 = y10
        z1 = z10

        #Matrix for positions
        X1 = []
        Y1 = []
        Z1 = []

        T=[]

        t = 0#Initial time
        ts = 1.5#Stop time
        counter = 0
        Vi = round(np.sqrt(x2*x2 + y2*y2 + z2*z2), 2)
        print("Initial velocity |v_o|={}m/s".format(Vi))

        while t<ts:
            #Calculating velocity
            if (modv(x2, y2, z2)>round(B2/0.3, 2)):
                Xii = x2 + (h/6)*(fx(x2,y2,z2)+4*fx(x2+.5*h,y2+.5*h,z2+.5*h)+fx(x2+h,y2+h,z2+h))
                Yii = y2 + (h/6)*(fy(x2,y2,z2)+4*fy(x2+.5*h,y2+.5*h,z2+.5*h)+fy(x2+h,y2+h,z2+h))
                Zii = z2 + (h/6)*(fz(x2,y2,z2)+4*fz(x2+.5*h,y2+.5*h,z2+.5*h)+fz(x2+h,y2+h,z2+h))
            else:
                Xii = x2 + (h/6)*(fxa(x2,y2,z2)+4*fxa(x2+.5*h,y2+.5*h,z2+.5*h)+fxa(x2+h,y2+h,z2+h))
                Yii = y2 + (h/6)*(fya(x2,y2,z2)+4*fya(x2+.5*h,y2+.5*h,z2+.5*h)+fya(x2+h,y2+h,z2+h))
                Zii = z2 + (h/6)*(fza(x2,y2,z2)+4*fza(x2+.5*h,y2+.5*h,z2+.5*h)+fza(x2+h,y2+h,z2+h))

            #Calculating position
            Xi = x1 + h*x2
            Yi = y1 + h*y2
            Zi = z1 + h*z2

            #Listting velocity and position in matrices
            X2.append(Xii)
            Y2.append(Yii)
            Z2.append(Zii)

            X1.append(Xi)
            Y1.append(Yi)
            Z1.append(Zi)
            T.append(t)
            #Putting new values
            x2 = Xii
            x1 = Xi
            y2 = Yii
            y1 = Yi
            z2 = Zii
            z1 = Zi
            t=t+h#incrementing time
            if(y1>=11):#checks the condition if the ball passes the goalpost
                break
            counter = counter+1
            

        i=0
        V=[]
        while (i<=counter):
            V.append(np.sqrt(X2[i]*X2[i] + Y2[i]*Y2[i] + Z2[i]*Z2[i]))
            i=i+1

        #Goalpost plot
        G1x = [-3.605, 0, 3.605]
        G1y = [11, 11, 11]
        G1z = [2.32, 2.32, 2.32]
        G2x = [-3.605, -3.605, -3.605]
        G2y = [11, 11, 11]
        G2z = [0, 1 , 2.32]
        G3x = [3.605, 3.605, 3.605]
        G3y = [11, 11, 11]
        G3z = [0, 1, 2.32]
        G4x = [2.605,3.605]
        G4y = [11, 11]
        G4z = [2.33, 1.72]

        Vf = round(np.sqrt(x2*x2 + y2*y2 + z2*z2), 2)
        print("Final velocity |v_f|={}m/s".format(Vf))
        print("(x,y,z)=({},{},{})".format(round(x1,2),round(y1, 2),round(z1, 2)))
        
        
        fig = plt.figure()
        ax = fig.add_subplot(1,2,1,projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.scatter3D(x1,y1,z1, color='black')#Final position of the ball
        #Goalpost
        ax.plot3D(G1x, G1y, G1z, color='r')
        ax.plot3D(G2x, G2y, G2z, color='r')
        ax.plot3D(G3x, G3y, G3z, color='r')
        ax.plot3D(G4x, G4y, G4z, color='r')
        ax.plot3D(X1,Y1,Z1)#Locus
        
        plt.subplot(1,2,2)
        plt.axvline(linewidth=1.1,color='b',linestyle='-')
        plt.axhline(linewidth=1.1,color='b',linestyle='-')
        plt.grid(color='y', linestyle='--', linewidth=.4)
        plt.title("$\|v|$ vs $t$ \n for initial $v$=({}, {}, {}) and angular velocity{} rad per s\n Final position, (x,y,z)=({} , {} , {} )\n Initial velocity |v_o|={}m/s \n Final velocity |v_f|={}m/s\n Goal time {}s".format(x20,y20,z20,round(B2/0.11, 2),round(x1,2),round(y1, 2),round(z1, 2), Vi, Vf,round(t, 2)))
        plt.xlabel("t in s")
        plt.ylabel("$|v|$ in $ms^{-1}$")
        plt.plot(T,V,'r*',markersize=.2)
        plt.tight_layout()
        figure = plt.gcf()
        figure.set_size_inches(12, 6)
        plt.savefig("angular_speed={}rad_per_s_Data_set_{}.jpeg".format((B2/0.11),lum+1 ), dpi=900)
        lum=lum+1
    B2=B2+1.1
