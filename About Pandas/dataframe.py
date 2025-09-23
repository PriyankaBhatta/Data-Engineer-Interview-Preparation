import pandas as pd

#Dataframe: A tabular data structure with rows and columns

data = {"Name": ["Priyanka", "Asbin", "Bhumika"],
        "Age": [23,25,24]
        }

df = pd.DataFrame(data, index = ["Employee 1: ", "Employee 2: ", "Employee 3: "])
print(df.loc["Employee 1: "]) # to find by location
print(df.iloc[1]) #to find by index

#add a new column
df["Job"] = ["Data Engineer", "Software Engineer", "CA"]

#add a new row
new_row = pd.DataFrame([{"Name": "Pramisha", "Age": 26, "Job": "Marketing Lead"}],
                       index=["Employee 4:"])
df = pd.concat([df, new_row])

# add new rows
new_rows = pd.DataFrame([{"Name": "Ayesha", "Age": 27, "Job": "Pilot"},
                         {"Name": "Ankita", "Age": 28, "Job": "ACCA"}],
                         index=["Employee 5:", "Employee 6:"])
df = pd.concat([df, new_rows])
print(df)



