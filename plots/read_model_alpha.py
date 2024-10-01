# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:14:18 2021

@author: keykh
"""

import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
# import config

dataPath = "../data/"
projectPath = dataPath + "rlb-dp/"



obj_type = "clk"
clk_vp = 1
N = 1000
c0 = 1 / 8
gamma = 1
alpha=[0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001,0.000000001]
src = "ipinyou"



num_tests=1

impression=np.zeros((num_tests,7))
click=np.zeros((num_tests,7))
cost=np.zeros((num_tests,7))
win_rate=np.zeros((num_tests,7))
cpm=np.zeros((num_tests,7))
alpha=np.zeros((num_tests,7))



#file1 = open(config.projectPath + "bid-performance/{}_N={}_c0={}_obj={}_clkvp={}.txt".format(config.src, config.N, config.c0, config.obj_type, config.clk_vp), "r")

#file_dir=projectPath + "bid-performance/samples/{}_N={}_c0={}_obj={}_clkvp={}.txt".format(src, N, c0, obj_type, clk_vp)
file_dir="model1_alpha_nextco.txt"
file1 = open(file_dir, "r")


content = file1.read()
#print(content)

content_list = content.split("\t")
file1.close()

#print(content_list[30])

for i in range(7):
    impression[0,i]=float(content_list[12+9*i])
    click[0,i]=float(content_list[13+9*i])
    cost[0,i]=float(content_list[14+9*i])
    win_rate[0,i]=float(content_list[15+9*i].replace('%', ''))
    cpm[0,i]=float(content_list[16+9*i])

    
print(win_rate)

# #x=np.array([1,2,3,4,5,6,7,8,9])

y1=np.zeros((1,7))
# y2=np.zeros((1,9))
# y3=np.zeros((1,9))
# y4=np.zeros((1,9))
# y5=np.zeros((1,9))

for i in range(7):
    y1[0,i]=click[0,i]
#     y2[0,i]=cpm[0,5*i+1]
#     y3[0,i]=cpm[0,5*i+2]
#     y4[0,i]=cpm[0,5*i+3]
#     y5[0,i]=cpm[0,5*i+4]

# #x=np.arange(1,10)
# plt.title("N={} , c0={}".format(N,c0))
# plt.xlabel('camp')
# plt.ylabel('win_rate')
#print(x[0])
#print(x)
str_month_list = ['1e -3','1e -4','1e -5','1e -6','1e -7','1e -8','1e -9']
x=[0,1,2,3,4,5,6]
plt.plot(x,y1[0],'b')

# plt.plot( y2[0],'r')
# plt.plot( y3[0],'g')
print(y1[0])
# plt.plot( y4[0], 'y')
# plt.plot( y5[0], 'c')
plt.legend(["rlb_smooth"])
#plt.legend([ "rlb" , "rlb_smooth"])
plt.title("N={} , c0={}".format(N,c0))
plt.xticks(x,str_month_list )
plt.xlabel('alpha')
plt.ylabel('click')
plt.savefig("{}_N={}_c0={}_obj={}_clkvp={}_alpha_click.jpg".format(src, N, c0, obj_type, clk_vp))
plt.show()
