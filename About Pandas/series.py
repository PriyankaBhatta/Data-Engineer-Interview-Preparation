import pandas as pd

print(pd.__version__)

#series = series one dimensional labelled array that can hold any data type

data = [101,102,104, 200, 202]
series = pd.Series(data, index=["a","b","c", "d", "e"])

series.loc["c"] = 200
print(series.loc["c"])
print(series.iloc[1])

print(series[series >= 200])
print(series[series < 200])

calories = {"Day 1": 1750,
            "Day 2": 2100,
            "Day 3": 1700}

series = pd.Series(calories)

print(series[series < 2000])
series.loc["Day 3"] +=500
print(series.loc["Day 3"])
