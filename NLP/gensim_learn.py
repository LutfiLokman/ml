from gensim.models import Word2Vec
import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/LutfiLokman/datasets/master/car_msrp.csv"
)

data["Maker_Model"] = data["Make"] + " " + data["Model"]

df1 = data[
    [
        "Engine Fuel Type",
        "Transmission Type",
        "Driven_Wheels",
        "Market Category",
        "Vehicle Size",
        "Vehicle Style",
    ]
]
df2 = df1.apply(lambda x: ",".join(x.astype(str)), axis=1)
df_clean = pd.DataFrame({"clean": df2})
sent = [row.split(",") for row in df_clean["clean"]]

sent_df = pd.DataFrame(sent)

model = Word2Vec(sent, min_count=1, workers=3, window=3, sg=1, vector_size=3)

model.wv['Hatchback']
model.wv.most_similar('MANUAL', topn=10)
