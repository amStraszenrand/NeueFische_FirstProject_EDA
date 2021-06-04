# %%
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as plx
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statsmodels.api as sms

# %%
df_raw = pd.read_csv("us_bank_wages/us_bank_wages.txt", delimiter = "\t", index_col=0)
df_raw

# %%
df = df_raw.copy()
df["GENDER_DENOTING"] = df_raw["GENDER"].replace({0 : "Female", 1 : "Male"})
df["MINORITY_DENOTING"] = df_raw["MINORITY"].replace({0 : "White", 1 : "Minority"})
df["JOBCAT_DENOTING"] = df_raw["JOBCAT"].replace({1 : "Administration", 2 : "Custody", 3 : "Management"})

df["SOCIODEMOGRAPHY"] = df_raw["GENDER"]*2**0 + df_raw["MINORITY"]*2**1
df["SOCIODEMOGRAPHY_DENOTING"] = df["MINORITY_DENOTING"].map(str) + "_" + df["GENDER_DENOTING"]

# %%
fig = plx.histogram(df,
    x = "SALARY",
    title = "Distribution of salaries"
)
fig.show()
# %%
fig = plx.scatter(df,
    x = "JOBCAT_DENOTING", 
    y = "SALARY",
    title = "Impact of Job Description on Salary"
)
fig.show()

# %%
fig = plx.scatter(df,
    x = "EDUC", 
    y = "SALARY", 
    color = "SALBEGIN",
    title = "Impact of Education and Entry Wage on Salary"
)
fig.update_traces(marker_size=12)
fig.show()

# %%
fig = plx.imshow(
    df.corr()
)
fig.show()

# %%
df_X = df.drop(columns = ["SALARY", "GENDER_DENOTING", "MINORITY_DENOTING", "JOBCAT_DENOTING", "SOCIODEMOGRAPHY_DENOTING"])
Y = df["SALARY"]
# %%
X_train, X_test, y_train, y_test = train_test_split(df_X, Y, test_size=0.4, random_state=17)
X_train


# %%
model = LinearRegression()
model.fit(X_train,y_train)


# %%
predictions = model.predict(X_test)

# %%
X_train_sms = sms.add_constant(X_train)
ls=sms.OLS(y_train,X_train_sms).fit()
print(ls.summary())
print("\n\n")

print(f"RMSE: {mean_squared_error(y_test, predictions)**0.5}")
# %%

# %%
