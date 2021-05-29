# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:37:31 2021

@author: szymek
"""

import numpy as np
import matplotlib.pyplot as plt
from RysujGeometrie import *

def RysujRozwiazanie(NODES, ELEMS, WB, u):

    
    RysujGeometrie(NODES,ELEMS,WB)
    
    x = NODES[:,1]
    
    plt.plot(x, u, 'm*')