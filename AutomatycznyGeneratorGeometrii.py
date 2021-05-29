# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:34:53 2021

@author: szymek
"""

import numpy as np

def AutomatycznyGeneratorGeometrii(a,b,n):

 
    lp = np.arange(1,n+1)
    x = np.linspace(a,b,n) ;        
    WEZLY = (np.vstack( (lp.T, x.T) )).T #[lp.T, x.T]

    
    lp = np.arange(1,n)
    C1 = np.arange(1,n)
    C2 = np.arange(2,n+1)
    ELEMENTY = (np.block( [[lp], [C1], [C2] ] ) ).T
                    
    return WEZLY, ELEMENTY