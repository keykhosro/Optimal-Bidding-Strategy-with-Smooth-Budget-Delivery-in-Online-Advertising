# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:48:24 2020

@author: khosro
"""
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
# import config
import pandas as pd
dataPath = "../data/"
projectPath = dataPath + "rlb-dp/"



obj_type = "clk"
clk_vp = 1
N = 1000
c0 = 1 / 16
gamma = 1

src = "ipinyou"



num_tests=1

impression=np.zeros((num_tests,45))
click=np.zeros((num_tests,45))
cost=np.zeros((num_tests,45))
win_rate=np.zeros((num_tests,45))
cpm=np.zeros((num_tests,45))



#file1 = open(config.projectPath + "bid-performance/{}_N={}_c0={}_obj={}_clkvp={}.txt".format(config.src, config.N, config.c0, config.obj_type, config.clk_vp), "r")

#file_dir=projectPath + "bid-performance/samples/{}_N={}_c0={}_obj={}_clkvp={}.txt".format(src, N, c0, obj_type, clk_vp)
file_dir="{}_N={}_c0={}_obj={}_clkvp={}.txt".format(src, N, c0, obj_type, clk_vp)

file1 = open(file_dir, "r")


content = file1.read()
#print(content)

content_list = content.split("\t")
file1.close()

#print(content_list[23])

for i in range(45):
    impression[0,i]=float(content_list[11+8*i])
    click[0,i]=float(content_list[12+8*i])
    cost[0,i]=float(content_list[13+8*i])
    win_rate[0,i]=float(content_list[14+8*i].replace('%', ''))
    cpm[0,i]=float(content_list[15+8*i])
    
#print(win_rate)

#x=np.array([1,2,3,4,5,6,7,8,9])

y1=np.zeros((9))
y2=np.zeros((9))
y3=np.zeros((9))
y4=np.zeros((9))
y5=np.zeros((9))
#y=np.zeros((4,9))
y=np.zeros((5,9))
#y=np.zeros((2,9))
for i in range(9):
    # y1[i]=win_rate[0,5*i+0]
    # y2[i]=win_rate[0,5*i+1]
    # y3[i]=win_rate[0,5*i+2]
    # y4[i]=win_rate[0,5*i+3]
    # y5[i]=win_rate[0,5*i+4]
    y[0,i]=win_rate[0,5*i+0]
    y[1,i]=win_rate[0,5*i+1]
    y[2,i]=win_rate[0,5*i+2]
    y[3,i]=win_rate[0,5*i+3]
    y[4,i]=win_rate[0,5*i+4]
    # y[0,i]=win_rate[0,5*i+3]
    # y[1,i]=win_rate[0,5*i+4]




df = pd.DataFrame(y.T, columns = ['ss_mdp','mcpc','lin_bid','rlb','rlb_smooth'])
#df = pd.DataFrame(y.T, columns = ['ss_mdp','mcpc','lin_bid','rlb'])
#df = pd.DataFrame(y.T, columns = ['rlb','rlb_smooth'])
#df = pd.DataFrame(y.T, columns = ['ss_mdp','mcpc','lin_bid','rlb'])
fig=df.plot( y=["ss_mdp", "mcpc" , "lin_bid" , "rlb" , "rlb_smooth"], kind="bar")
#fig=df.plot( y=["ss_mdp", "mcpc" , "lin_bid" , "rlb" ], kind="bar")
#fig=df.plot( y=[ "rlb" , "rlb_smooth"], kind="bar")
fig.set_xlabel("camp")
fig.set_ylabel("win_rate")
#fig.suptitle('N=1000 , c0=0.0625')
#ig=df.plot( y=["ss_mdp", "mcpc" , "lin_bid" , "rlb" ], kind="bar")
fig.figure.savefig("newfn_{}_N={}_c0={}_obj={}_clkvp={}_winrate_all.jpg".format(src, N, c0, obj_type, clk_vp))
x=np.arange(1,10)
plt.title("N={} , c0={}".format(N,c0))
plt.xlabel('camp')
plt.ylabel('win_rate')
#print(x[0])
#print(x)
# plt.plot( y1,'b')
# plt.plot( y2,'r')
# plt.plot( y3,'g')
# #print(y4)
# plt.plot( y4, 'y')
# #plt.plot( y5, 'c')
# #plt.legend(["ss_mdp", "mcpc" , "lin_bid" , "rlb" , "rlb_smooth"])
# plt.legend(["ss_mdp", "mcpc" , "lin_bid" , "rlb" ])
# #plt.legend([ "rlb" , "rlb_smooth"])
# plt.title("N={} , c0={}".format(N,c0))
# plt.xlabel('camp')
# plt.ylabel('win_rate')
# plt.savefig("newf_{}_N={}_c0={}_obj={}_clkvp={}_win_rate_all.jpg".format(src, N, c0, obj_type, clk_vp))
# plt.show()



