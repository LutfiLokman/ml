import pandas as pd
import json

data = pd.read_csv(
    "~/OneDrive/Desktop/data.csv",
    nrows=1000,
)


data["Maker_Model"] = data["Make"] + " " + data["Model"]

df = data[
    [
        "Transmission Type",
        "Vehicle Size",
        "Vehicle Style",
        "Maker_Model",
    ]
]


df["json"] = df.apply(
    lambda x: '"{}":"{}"'.format(x["Maker_Model"], x["Vehicle Style"]), axis=1
)

df_gp = (
    df.groupby("Maker_Model")
    .agg(
        {
            "Maker_Model": "first",
            "Vehicle Size": "first",
            "Transmission Type": lambda x: ", ".join(x.unique()),
            "json": lambda x: ", ".join(x.unique()),
        }
    )
    .reset_index(drop=True)
)

df_gp = df_gp[df_gp["Maker_Model"].str.contains("Chrysler")]
df_gp["json"] = df_gp["json"].apply(lambda x: "{{{}}}".format(x))
df_gp["type"] = df_gp["json"].apply(lambda x: list(json.loads(x).values())[0])
