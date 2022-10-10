# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:41:51 2022

@author: steenbergenhvan1
"""

from matplotlib import pyplot as plt
import os

import numpy as np

from datamatrix import DataMatrix, io, operations as ops

import pandas as pd


pygame.

# see https://osdoc.cogsci.nl/3.3/manual/logging/




# data from https://osf.io/3d9er


df = pandas.read_csv('data/subject-0_CI.csv')
print(df)

#get all column names?
df


from datamatrix import io

dm = io.readtxt('data/subject-0_CI.csv')
print(dm)



# Change this to the folder that contains the .csv files
SRC_FOLDER = 'data'
# Change this to a list of column names that you want to keep
COLUMNS_TO_KEEP = [
    'subject_nr',
    'congruency',
    'response_time',
    'acc'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Reading {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'merged-data.csv')

dm = io.readtxt('merged-data.csv')
df = pd.read_csv('merged-data.csv')


plt.plot(dm.subject_nr, dm.acc, ',')

#check counts
pandas.pivot_table(
    dm,
    values="acc",
    index=["subject_nr"],
    columns=["congruency"],
    aggfunc=len,
)


#datamatrix syntax
plt.figure(figsize=(8,6))
plt.hist((dm.congruency == 'con').response_time, bins=100, alpha=0.5, label="data1")
plt.hist((dm.congruency == 'inc').response_time, bins=100, alpha=0.5, label="data2")

#dataframe syntax
plt.figure(figsize=(8,6))
plt.hist(df.query("congruency == 'con'").response_time, bins=100, alpha=0.5, label="data1")
plt.hist(df.query("congruency == 'inc'").response_time, bins=100, alpha=0.5, label="data2")


import seaborn as sns

sns.set_theme(style="darkgrid")
sns.displot(
    df, x="response_time", col="congruency", row="subject_nr",
    binwidth=10, height=3, facet_kws=dict(margin_titles=True),
)


