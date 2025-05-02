import pandas as pd
#series is 1d array in pandas
#dataframe is normally 2d array having rows and columns in pandas

#encoding=files to computer understandble form "latin1"
df= pd.read_csv("students.xlsx",encoding="latin1")
print(df)

