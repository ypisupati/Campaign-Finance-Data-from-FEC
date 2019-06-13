# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:01:28 2019

@author: Yasaswi Pisupati
"""
import pandas as pd
import numpy as np
import matplotlib
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

import data_import

total_data = pd.concat([data_87_88, data_89_90, data_91_92, data_93_94,
                        data_95_96, data_97_98, data_99_00, data_01_02, 
                        data_03_04, data_05_06, data_07_08, data_09_10,
                        data_11_12, data_13_14, data_15_16, data_17_18], axis = 0)