 #! /usr/bin/env python3
import pandas as pd
flightdelay=pd.read_csv("flightdelays.csv")
flightdelay[flightdelay['Origin']=='SFO']['ArrDelay'].iloc[:3]