import pandas as pd

# read csv from a github repo
df = pd.read_csv("./bank-marketing-analysis.csv")

print(df.head(10))