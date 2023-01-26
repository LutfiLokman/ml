import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/narxiss24/datasets/master/titanic_train.csv"
)

# <leader>rp/b - Print in console/in browser
# <leader>rl - Print length
# <leader>rs - Print summary
# <leader>ri/I - Print columns/info
df

# <leader>rt - Frequency table
df["Pclass"]
df["Sex"]

# <leader>rg - Plot histogram
# <leader>rG - Plot histogram excluding outliers
df["Fare"]

df_copy = df.copy()
# <leader>r/W - Show/delete local variables
