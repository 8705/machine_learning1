# -*- coding: utf-8 -*-
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def M(m):
    return np.sum(m,axis =0)[1] + np.sum(m,axis = 1)[1] - m[1][1]

def f(x):
    if x == 2 or x==0 or x==1:
        return 0
    else:
        return 1

plt.clf()
N1 = 20
fig = plt.figure()
ims =[]

a = np.copy([[0]*N1]*N1)
for i in range(3):
    a[5][5+i]=1
for i in range(3):
    a[5+i][7]=1
for i in range(5):
    a[3][5-i]=1
for i in range(3):
    a[3-i][7]=1

a[10][10]=1
a[11][10]=1
a[10][11]=1
a[11][11]=1
a[11][12]=1
a[11][13]=1
a[12][13]=1
a[13][13]=1
a[12][13]=1
a[10][11]=1
a[10][9]=1
a[10][9]=1
a[9][10]=1
a[8][10]=1


a[15][15]=1
a[14][15]=1
a[13][15]=1
a[13][16]=1
a[13][17]=1
a[13][18]=1
a[12][18]=1
a[11][18]=1
a[10][18]=1

for i in range(N1):
    a[i][4]=1

aa = [[0]*N1]*N1
aa = np.array(aa)
print(np.all(a==aa))
print(np.any(a!=aa))
n=0
while np.any(a!=aa):
    n=n+1
    aa=np.copy(a)
    b = np.random.randint(0,2,(N1,1)).astype(int)
    c = np.ones([1,N1+2]).astype(int)
    d = np.copy(np.hstack((b,a,b)))
    g = np.vstack((c,d,c))

    im = plt.imshow( aa, interpolation='none' )
    ims.append([im])
    print(a)
    e = [[
     [[g[j][i] for i in range(m,m+3)] for j in range(n,n+3) ] for m in range(N1)] for n in range(N1)]
    D = [[M(e[i][j]) for j in range(N1)] for i in range(N1)]
    Dnew = np.array(D)

    for i  in range(N1):
        for j in range(N1):
            a[i][j]=f(Dnew[i][j])*a[i][j]

    print("ステップ数",n)


aa = [[0]*N1]*N1
while  np.any(a!=aa):
    qaa=np.copy(a)
    b = np.random.randint(0,2,(N1,1)).astype(int)
    c =  np.ones([1,N1+2]).astype(int)
    c10 =10*c
    d = np.copy(np.hstack((b,a,b)))
    g = np.vstack((c10,d,c))
    print(aa)
    im = plt.imshow( aa, interpolation='none' )
    #im = sns.heatmap(g, cbar=False,linewidths=.5)

    ims.append([im])

    Dnew = np.array(D)
    for i  in range(1,N1+1):
        for j in range(1,N1+1):
            if ( g[i-1][j] == 10 or g[i][j-1] == 10 or g[i+1][j] == 10 or g[i][j+1] == 10) and g[i][j]==1:
                a[i-1][j-1]=10
            else:
                a[i-1][j-1]=a[i-1][j-1]

for i  in range(N1):
    for j in range(N1):
        if a[i][j]==1:
            a[i][j]=0
        else:
            a[i][j]=a[i][j]

aa=np.copy(a)
im = plt.imshow( aa, interpolation='none' )
#im = sns.heatmap(g, cbar=False,linewidths=.5)

ims.append([im])
ani = animation.ArtistAnimation(fig,ims,interval = 1000, repeat_delay = 2000000)
plt.show(ani)
