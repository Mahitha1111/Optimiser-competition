# -*- coding: utf-8 -*-
"""Copy of Optimzer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19hqelNpRW4GUMLL94SmY1smtIEzY-H7x
"""

!pip install nevergrad

import numpy as np
import nevergrad as ng
import random

def myfun1(x,y):
    return (x-270)**2 + (y-53)**2 + x*y + random.random()

def myfun2(x,y):
    return ( x/263 + 6*y/54-7 )**2 + ( 2*x/263 + 3*y/54-5 )**2 #booth function

# As given in the problem statement
params = ng.p.Instrumentation(
    x=ng.p.Array(shape=(1,),lower=250,upper=300),
    y=ng.p.Array(shape=(1,),lower=50,upper=60)
)

algos = sorted(ng.optimizers.registry.keys())

algos

for algo in algos:
    try:
        optimizer = ng.optimizers.registry[algo](parametrization=params, budget=7, num_workers=1)
        for _ in range(optimizer.budget):
            x = optimizer.ask()
            loss = myfun2(*x.args, **x.kwargs)
            optimizer.tell(x, loss)

        recommendation = optimizer.provide_recommendation()

        x_opt = recommendation.value[1]['x']
        y_opt = recommendation.value[1]['y']
        # if myfun(x_opt,y_opt)<1:
        print('Algo',algo,' Score:',myfun2(x_opt,y_opt),' x:',x_opt,' y:',y_opt)
    except:
        continue

# Actual Model

#!pip install nevergrad
import nevergrad as ng

params = ng.p.Instrumentation(
    x=ng.p.Array(shape=(1,),lower=250,upper=300),
    y=ng.p.Array(shape=(1,),lower=50,upper=60)
)

# print(sorted(ng.optimizers.registry.keys())) # to display all availabe algorithms
algo = 'ES'
optimizer = ng.optimizers.registry[algo](parametrization=params, budget=20, num_workers=1)

while True:
    x = optimizer.ask()
    loss = input(f"{x.value[1]['y']},{x.value[1]['x']}")
    loss = float(loss)
    optimizer.tell(x,loss)