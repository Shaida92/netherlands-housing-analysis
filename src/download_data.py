import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://opendata.cbs.nl/ODataApi/OData/83625ENG/TypedDataSet?$top=20"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["value"])

df["Year"] = df["Periods"].str[:4]

plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["AveragePurchasePrice_1"])
plt.title("Average House Prices in the Netherlands")
plt.xlabel("Year")
plt.ylabel("Average Purchase Price (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/house_prices.png")