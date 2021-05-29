# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:33:00 2021

@author: szymek
"""

import numpy as np

def Aij(df_i, df_j, c, f_i, f_j):

    return lambda x: -df_i(x)*df_j(x) + c*f_i(x)*f_j(x)  # fun_podc