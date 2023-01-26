import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import wooldridge as woo
from statsmodels.formula.api import ols

df = woo.dataWoo("kielmc")

df["rprice"] = df["rprice"] / 1000

mdl78 = ols("rprice ~ rooms + area", data=df).fit()

mdl78.summary()

# Surface visualization
x_surf, y_surf = np.meshgrid(
    np.linspace(df["rooms"].min(), df["rooms"].max(), 100),
    np.linspace(df["area"].min(), df["area"].max(), 100),
)

onlyX = pd.DataFrame({"rooms": x_surf.ravel(), "area": y_surf.ravel()})
fittedY = np.array(mdl78.predict(exog=onlyX))
fittedY = fittedY.reshape(x_surf.shape)

fig = px.scatter_3d(
    x=df["rooms"],
    y=df["area"],
    z=df["rprice"],
    color=df["rooms"],
    color_continuous_scale="Viridis",
    labels={"x": "rooms", "y": "area", "z": "rprice"},
    title="Predicted House Prices",
    template="plotly_dark",
)

fig.update_traces(marker=dict(size=6))
fig.add_traces(go.Surface(z=fittedY, x=x_surf, y=y_surf, opacity=0.5))

fig.show()
