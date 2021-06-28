import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv("house_data_ultimate_cleaned",index_col="Unnamed: 0")
print(df.columns)
df.drop(columns=["open_fire", "type_property"], axis=1, inplace=True)

def zip_to_province(x):
    flanders = "Flanders"
    wallonia = "Wallonia"
    if x in range(1000,1300):
        return "Brussels"
    elif x in range(1300,1500):
        return wallonia
    elif x in range(1500,4000):
        return flanders
    elif x in range(4000,8000):
        return wallonia
    elif x in range(8000,10000):
        return flanders


df["regions"] = df["zip_code"].apply(lambda x: zip_to_province(x))


