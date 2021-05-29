# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:36:02 2021

@author: szymek
"""

import numpy as np

def GeometriaDefinicja():
    
    WEZLY = np.array([[1, 0], 
                      [2, 1], 
                      [3, 0.5], 
                      [4, 0.75]] ) 
       
    ELEMENTY = np.array( [[1, 1, 3], 
                       [2, 4, 2], 
                       [3, 3, 4]] )
    # w postaci krotek: nr_wezla, typ_warunku, wartosc
    # przy pomocy slownika
    WB    = [{"ind": 1, "typ":'D', "wartosc":1}, 
             {"ind": 2, "typ":'D', "wartosc":2}]

    return WEZLY, ELEMENTY, WB