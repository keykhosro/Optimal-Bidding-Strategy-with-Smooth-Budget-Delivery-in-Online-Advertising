# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:42:36 2020

@author: khosro
"""
import numpy as np
import matplotlib.pyplot as plt

dataPath = "../data/"
projectPath = dataPath + "rlb-dp/"

#N_=[200 ,400 , 600 , 800 ,1000]
N_=[200 , 400 , 600 ,800,1000]
c0_=[1/32 ,1/16 ,1/8 ,1/4 ,1/2]

obj_type = "clk"
clk_vp = 1
gamma = 1

src = "ipinyou"

num_tests=5

impression=np.zeros((num_tests,36))
click=np.zeros((num_tests,36))
cost=np.zeros((num_tests,36))
win_rate=np.zeros((num_tests,36))
cpm=np.zeros((num_tests,36))
state=np.zeros((num_tests,2))

for N in N_:
    KK=0
    for c0 in c0_:
        file_dir=projectPath + "bid-performance/samples/{}_N={}_c0={}_obj={}_clkvp={}.txt".format(src, N, c0, obj_type, clk_vp)
        file1 = open(file_dir, "r")
        content = file1.read()
        #print(content)
        content_list = content.split("\t")
        ############################## debug
        file1.close()
        for i in range(36):
            impression[(N/200 -1)*5+KK ,i]=float(content_list[11+8*i])
            click[(N/200 -1)*5+KK,i]=float(content_list[12+8*i])
            cost[(N/200 -1)*5+KK,i]=float(content_list[13+8*i])
            win_rate[(N/200 -1)*5+KK,i]=float(content_list[14+8*i].replace('%', ''))
            cpm[(N/200 -1)*5+KK,i]=float(content_list[15+8*i])
        state[(N/200 -1)*5+KK,0]=N
        state[(N/200 -1)*5+KK,1]=c0
        KK=KK+1











################################### N is consistant
# for N = 800 constant
n0=200
p=1 # one of the 9 camp random

y1=np.zeros((1,5))
y2=np.zeros((1,5))
y3=np.zeros((1,5))
y4=np.zeros((1,5))

for i in range(5):
    y1[0,i]=win_rate[(n0/200 -1)*5+i,p*4]
    y2[0,i]=win_rate[(n0/200 -1)*5+i,p*4 +1]
    y3[0,i]=win_rate[(n0/200 -1)*5+i,p*4 +2]
    y4[0,i]=win_rate[(n0/200 -1)*5+i,p*4 +3]





#x=np.arange(1,10)
# plt.title("N={} , c0={}".format(N,c0))
# plt.xlabel('camp')
# plt.ylabel('win_rate')
#print(x[0])
#print(x)
plt.plot( c0_ , y1[0],'b')
plt.plot(  c0_ , y2[0],'r')
plt.plot(  c0_ , y3[0],'g')
plt.plot(  c0_ , y4[0], 'y')
plt.legend(["ss_mdp", "mcpc" , "lin_bid" , "rlb"])
plt.title("N={} , camp={} ".format(n0 , p))
plt.xlabel('c0')
plt.ylabel('win_rate')
plt.savefig(projectPath + "bid-performance/samples/{}_N={}_camp={}_obj={}_clkvp={}.jpg".format(src, N, p, obj_type, clk_vp))
plt.show()







################################### c0 is consistant
# for c0 = 1/8 constant
c0=1/8
p=1 # one of the 9 camp random
c_index=c0_.index(c0)
y1=np.zeros((1,5))
y2=np.zeros((1,5))
y3=np.zeros((1,5))
y4=np.zeros((1,5))

for i in range(5):
    y1[0,i]=win_rate[i*5+c_index,p*4]
    y2[0,i]=win_rate[i*5+c_index,p*4 +1]
    y3[0,i]=win_rate[i*5+c_index,p*4 +2]
    y4[0,i]=win_rate[i*5+c_index,p*4 +3]





#x=np.arange(1,10)
# plt.title("N={} , c0={}".format(N,c0))
# plt.xlabel('camp')
# plt.ylabel('win_rate')
#print(x[0])
#print(x)
plt.plot( N_ , y1[0],'b')
plt.plot(  N_ , y2[0],'r')
plt.plot(  N_ , y3[0],'g')
plt.plot(  N_ , y4[0], 'y')
plt.legend(["ss_mdp", "mcpc" , "lin_bid" , "rlb"])
plt.title("c0={} , camp={} ".format(c0 , p))
plt.xlabel('N')
plt.ylabel('win_rate')
plt.savefig(projectPath + "bid-performance/samples/{}_c0={}_camp={}_obj={}_clkvp={}.jpg".format(src, c0, p, obj_type, clk_vp))
plt.show()
