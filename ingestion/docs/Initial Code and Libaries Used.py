import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url = "https://api.census.gov/data/2024/acs/acs5"
response = requests.get(url)
data = response.json()
url2 = "https://data.montgomerycountymd.gov/api/v3/views/7bhj-887p/query.json?app_token=8kUbrmGzgoxqe4z7C91iV3wmC"
response2 = requests.get(url2)
data2 = response2.json()
df_bias = pd.DataFrame(data2)
