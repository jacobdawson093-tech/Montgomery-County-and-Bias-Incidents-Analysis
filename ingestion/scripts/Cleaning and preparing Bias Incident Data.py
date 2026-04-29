# Convert 'incident_date' to datetime
df2['incident_date'] = pd.to_datetime(df2['incident_date'])

# Create a binary 'resolved' column from 'status'
df2['resolved'] = df2['status'].apply(lambda x: 1 if x in ['Closed-Admin', 'Closed-Investigation', 'Closed-Exception', 'Closed-Arrest'] else 0)

# Convert suspect age columns to numeric, coercing errors to NaN
df2['suspects_less_than_18_years'] = pd.to_numeric(df2['suspects_less_than_18_years'], errors='coerce').fillna(0).astype(int)
df2['suspects_18_35_years_old'] = pd.to_numeric(df2['suspects_18_35_years_old'], errors='coerce').fillna(0).astype(int)
df2['suspects_36_45_years_old'] = pd.to_numeric(df2['suspects_36_45_years_old'], errors='coerce').fillna(0).astype(int)
df2['suspects_46_55_years_old'] = pd.to_numeric(df2['suspects_46_55_years_old'], errors='coerce').fillna(0).astype(int)
df2['suspects_55_years_old'] = pd.to_numeric(df2['suspects_55_years_old'], errors='coerce').fillna(0).astype(int)

# Create a binary variable for incidents with suspects under 18
df2['under_18_suspect'] = df2['suspects_less_than_18_years'].apply(lambda x: 1 if x > 0 else 0)

#Create bias category to seperate religious bias to racial/ethnic biases
def categorize_bias(bias_code):
    religious_biases = ['Anti-Jewish', 'Anti-Muslim', 'Anti-Catholic', 'Anti-Sikh', 'Anti-Hindhu', 'Anti-Protestant', 'Anti-Buddhist']
    racial_ethnic_biases = ['Anti-Black', 'Anti-White', 'Anti-Asian', 'Anti-Hispanic', 'Anti-Multi-Racial', 'Anti-American Indian', 'Anti-Other Race/Ethnicity']

    if bias_code in religious_biases:
        return 'Religious Bias'
    elif bias_code in racial_ethnic_biases:
        return 'Racial/Ethnic Bias'
    else:
        return 'Other Bias' # For categories not explicitly religious or racial/ethnic

df2['bias_category'] = df2['bias_code'].apply(categorize_bias)
