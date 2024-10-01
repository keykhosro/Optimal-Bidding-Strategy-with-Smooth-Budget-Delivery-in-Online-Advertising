# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 08:23:30 2021

@author: keykh
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#import pandas as pd
# import config



obj_type = "clk"
clk_vp = 1
N = 1000
c0 = 1 / 8
gamma = 1

src = "ipinyou"

camp=1485

#algo="rlb"
algo="rlb_smooth"
alpha=0.1
num_tests=1






#file_dir="{}, camp={}, algo={}, N={}, c0={}.txt".format(src, camp, algo, N, c0)
#file_dir="{}, camp={}, algo={}, N={}, c0={}_{}.txt".format(src, camp, algo, N, c0,alpha)


#file_dir="ipinyou, camp=1458, algo=rlb, N=1000, c0=0.125.txt"

file_dir="ipinyou, camp=1458, algo=rlb_smooth, N=1000, c0=0.125_0.1.txt"


file1 = open(file_dir, "r")


content = file1.read()
#print(content)

content_list = content.split("\t")
file1.close()

#print(content_list[5997])

num=np.size(content_list)
#print(num)

episode_num=int(num/(N*3))
#print(episode_num)

cost=np.zeros((episode_num,N))
bid=np.zeros((episode_num,N))


for i in range(350000):
    a=math.floor(i/1000)
    cost[a,i-a*1000]=content_list[i*3+1]
    bid[a,i-a*1000]=content_list[i*3+2]

#print(cost[6,:])
#print(bid[6,:])




plt.plot(cost[6,:],'b')

plt.legend([ "rlb_smooth" ])
#plt.legend([ "rlb" , "rlb_smooth"])
plt.title("N={} , c0={} , alpha={}".format(N,c0,alpha))
plt.xlabel('auctions')
plt.ylabel('budget')
plt.savefig("episode7_cost"+"algo={}_{}_camp={}_N={}_c0={}_obj={}_clkvp={}_click_all_alpha={}.jpg".format(algo,src,camp, N, c0, obj_type, clk_vp,alpha))
plt.show()
