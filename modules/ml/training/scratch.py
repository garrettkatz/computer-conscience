import pandas as pd

datraw = pd.read_csv("data/compas-scores-raw.csv")
dat = pd.read_csv("data/compas-scores.csv")
dat2y = pd.read_csv("data/compas-scores-two-years.csv")
dat2yv = pd.read_csv("data/compas-scores-two-years-violent.csv")

print("raw")
print(datraw.loc[0,:])

print("dat")
# print(dat.loc[0,:])
print(dat.columns)

print("2y")
# print(dat2y.loc[0,:])
print(dat2y.columns)

print("2yv")
print(dat2yv.loc[0,:])
# print(dat2yv.columns)
