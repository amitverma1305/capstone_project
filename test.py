#!/usr/bin/env python3
import pandas as pd
flightdelay=pd.read_csv("flightdelays.csv")
data=flightdelay[flightdelay['Origin']=='SFO']['ArrDelay'].iloc[:3]
data.to_csv('first3sfo.csv')
c=pd.read_csv('first3sfo.csv',header=None)[1]
print(c)
print(flightdelay['Dest'].value_counts().head(3))
print("Amit Verma")
