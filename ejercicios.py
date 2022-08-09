# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:41:15 2022

@author: Administrador
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline
import warnings
warnings.filterwarnings("ignore")

from alpha_vantage.timeseries import TimeSeries

key="CSA27SHO1NP6VZEW"

ts=TimeSeries(key, output_format='pandas')
amzn, _= ts.get_daily(symbol='AMZN', outputsize='full')
