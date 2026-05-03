import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chi2_contingency
import numpy as np
import statsmodels.formula.api as smf
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, RocCurveDisplay
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import datetime
import os
os.makedirs("graphs", exist_ok=True)

url = "https://api.census.gov/data/2024/acs/acs5"
response = requests.get(url)
data = response.json()
url2 = "https://data.montgomerycountymd.gov/api/v3/views/7bhj-887p/query.json?app_token=8kUbrmGzgoxqe4z7C91iV3wmC"
response2 = requests.get(url2)
data2 = response2.json()

df1 = pd.DataFrame(data)

df2 = pd.DataFrame(data2)
df2.head()
