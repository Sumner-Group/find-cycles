#!/usr/bin/env python
# coding: utf-8

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys
import math


if(len(sys.argv)<6):
    print("This script requires the following arguments (arguments in [] are optional:")
    print("<InputFile> <OutputFile> <# Molecules> <Name of residue> <Name of oxygen> <Name of hydrogen> [distance cutoff] [angle cutoff] [max number of molecules in a cycle]")
    print("Defaults are: [distance cutoff]=3.2 [angle cutoff]=130 [max number of molecules in a cycle]=10")
    sys.exit()
#Input Variables
InputFile = sys.argv[1]
OutputFile = sys.argv[2]
NumMolec = int(sys.argv[3])
resname = sys.argv[4]
oxygen = sys.argv[5]
hydrogen = sys.argv[6]
#NumMolec=256
outfile= open(OutputFile,"w")
infile= open(InputFile,"r")
distcut=3.2
angcut=130.0
cyccut=10
if(len(sys.argv)>=8):
    distcut=float(sys.argv[7])
if(len(sys.argv)>=9):
    angcut=float(sys.argv[8])
if(len(sys.argv)==10):
    cyccut=float(sys.argv[9])
    
# Initialize variables/arrays/lists
i = 0
j = 0
k = 0
l = 0
positionsO = []
positionsH = []
nodeO = []
nodeH = []
numat = []
DistMat = np.empty((NumMolec,NumMolec),dtype=int)
outfile.write("Cycle **** Cycle Length **** Geoemtry Number\n")
#Read in input file one line at a time
lines = infile.readlines()
for x in lines:

    if(len(x)>80):
        name2 = x.split()[2]
        name3 = x.split()[3]
#Read in oxygen and hydrogen positions
        if(name3 == resname and name2 == oxygen):
            for k in range(3):
                positionsO.append(float(x.split()[k+5]))
        elif(name3 == resname and name2 == hydrogen):
            #rint(x,i)
            for k in range(3):
                positionsH.append(float(x.split()[k+5]))
            i+=1
    
    if(x.split()[0] == "ENDMDL"):
#Make a distance matrix. DistMat[j,j]=1 if the distance between oxygen atoms is less than distance cutoff and if the
# Donor-H-Acceptor angle is greater than angle cutoff. Otherwise it's 0
        DistMat[:]=0
        for j in range(i):
            for k in range(i):
                a=np.array((positionsO[3*j+0],positionsO[3*j+1],positionsO[3*j+2]))
                b=np.array((positionsO[3*k+0],positionsO[3*k+1],positionsO[3*k+2]))
                c=np.array((positionsH[3*k+0],positionsH[3*k+1],positionsH[3*k+2]))
                dist=np.linalg.norm(a-b)
                dist2=np.linalg.norm(c-b)
                dist3=np.linalg.norm(c-a)
                dot=np.dot(b-c,a-c)
                if(k!=j):
                    dot=dot/(dist3*dist2)
                    ang = np.arccos(dot)/np.pi*180
                    if(dist<distcut and ang > angcut):
                        DistMat[k,j]=1
#Turn distance matrix into a directed graph, G
        G=nx.from_numpy_matrix(DistMat,parallel_edges=False,create_using=nx.DiGraph)
#Locate simple cycles, G2
        G2=nx.simple_cycles(G)
#Print out cycle information if the cycle is less than cycle cutoff and greater than 2
        sum = 0
        for x in G2:
            y=np.array(x)
            if (len(y)<cyccut and len(y)>2):
                sum+=len(y)
                outfile.write("%s %s %s\n" % (x,len(x),l))
        outfile.write("Percent %s\n" % (sum/NumMolec*100))
#Clear the hydrogen and oxygen position lists
        positionsO = []
        positionsH = []
        l+=1
        i=0
outfile.close()
infile.close()





