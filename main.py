#!/usr/bin/env python

"""Plot my equities

"""
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("equities.2017", parse_dates=[0], index_col=[0])
data.plot()
plt.show()
