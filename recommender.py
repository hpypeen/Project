import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("data/data.csv", on_bad_lines="skip")

# Drop the missing values
# we have over 100K in the dataframe
df = df.dropna()

# Format the column
df.columns = df.columns.str.replace('"', "").str.strip()

# Remove the duplicate songs
df = df.drop_duplicates(subset="trackname")

# Drop the user_id column
df = df.drop("user_id", axis=1)

# print(df.duplicated(subset="").sum())
print(df)