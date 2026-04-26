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
