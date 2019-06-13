# -*- coding: utf-8 -*-
"""
Created on Wed Jun#2 10:46:55 2019

@author: Yasaswi Pisupati
"""


#try to define a process for importing the csv files of capaign finance data

import pandas as pd
import numpy as np
import matplotlib
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

def data_import(csv):
    data = pd.read_csv(csv)
    Candidates = data[['Candidate identification', 'Candidate name', 'Party affiliation', 'Incumbent challenger status', 'General election percentage', 'Total individual contributions',
                  'Contributions from other political committees', 'Contributions from party committees',
                   'Primary election status', 'General election status']]
    Candidates = Candidates.fillna(0)
    #real_cand = Candidates[Candidates['Total individual contributions'] != 200]
    
    #return real_cand
    return Candidates


data_87_88 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1987-1988%20candidate%20results.csv')
year_1988 = [1988]*2283
data_87_88['year'] = year_1988

data_89_90 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1989-1990%20candidate%20results.csv')
year_1990 = [1990]*2213
data_89_90['year'] = year_1990   

data_91_92 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1991-1992%20candidate%20results.csv')
year_1992 = [1992]*3016
data_91_92['year'] = year_1992

data_93_94 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1993-1994%20candidate%20results.csv')
year_1994 = [1994]*3103
data_93_94['year'] = year_1994

data_95_96 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1995-1996%20candidate%20results.csv')
year_1996 = [1996]*3045
data_95_96['year'] = year_1996

data_97_98 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1997-1998%20candidate%20results.csv')
year_1998 = [1998]*2631
data_97_98['year'] = year_1998

data_99_00 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/1999-2000%20candidate%20results.csv')
year_2000 = [2000]*2604
data_99_00['year'] = year_2000

data_01_02 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2001-2002%20candidate%20results.csv')
year_2002 = [2002]*2445
data_01_02['year'] = year_2002

data_03_04 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2003-2004%20candidate%20results.csv')
year_2004 = [2004]*2468
data_03_04['year'] = year_2004

data_05_06 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2005-2006%20candidate%20results.csv')
year_2006 = [2006]*2410
data_05_06['year'] = year_2006

data_07_08 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2007-2008%20candidate%20results.csv')
year_2008 = [2008]*2600
data_07_08['year'] = year_2008

data_09_10 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2009-2010%20candidate%20results.csv')
year_2010 = [2010]*3173
data_09_10['year'] = year_2010

data_11_12 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2011-2012%20candidate%20results.csv')
year_2012 = [2012]*3271
data_11_12['year'] = year_2012

data_13_14 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2013-2014%20candidate%20results.csv')
year_2014 = [2014]*2989
data_13_14['year'] = year_2014

data_15_16 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2015-2016%20candidate%20results.csv')
year_2016 = [2016]*2906
data_15_16['year'] = year_2016

data_17_18 = data_import('https://raw.githubusercontent.com/ypisupati/Campaign-Finance-Data-from-FEC/master/2017-2018%20candidate%20results.csv')
year_2018 = [2018]*3683
data_17_18['year'] = year_2018
