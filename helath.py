import pandas as pd
df=pd.read_csv("indian_diseases_dataset.csv")
print(df.head(5))
print(df.info)

#finding duplicates
print(df.isnull().sum())

'''
print(df.isnull().sum())
here This command takes that True/False map from above and adds up the results for each column.  
In Python, True acts as the number 1 and False acts as 0.'''

print(df.isnull())

'''True = The data is missing (NaN/Null).

False = The data is present.'''
#filling ht enull values here unknown is the word replaces null

df['comorbidity'].fillna('Unknown', inplace=True)
df['alcohol_use'].fillna('Unknown', inplace=True)

print(df.isnull().sum())
df['cause_of_death'].fillna('Not Applicable', inplace=True)
df['recovery_days'].fillna(df['recovery_days'].median(), inplace=True)

'''EX:
5, 6, 7, 8, 10, 12, NaN, NaN

Median = 7.5 (middle value)

3 Then all missing values are replaced with that same median value.

Result:

5, 6, 7, 8, 10, 12, 7.5, 7.5
'''
print(df.isnull().sum())

# her index=false is used because if not index takes separte (line forms in table)

#saving back to the xl file after cleaning

df.to_csv("cleaned_dataset.csv", index=False)

