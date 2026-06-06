import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://opendata.cbs.nl/ODataApi/OData/83625ENG/TypedDataSet?$top=20"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["value"])

plt.plot(df["AveragePurchasePrice_1"])
plt.savefig("charts/house_prices.png")