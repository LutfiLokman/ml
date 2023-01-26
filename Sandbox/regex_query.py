import pandas as pd

df = pd.DataFrame({"values": ["766", "767", "768.00"]})

query_str = "values.str.match('420', case=False)"

results = df.query(query_str)


def times_two(x):
    x = x * 2

    return x


print(times_two(2))
