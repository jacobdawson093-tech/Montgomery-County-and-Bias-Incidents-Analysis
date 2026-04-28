# 1. Map Police Districts to Cities
# Based on the provided police district information:
district_to_city_map = {
    '1D': 'Rockville',
    '2D': 'Bethesda',
    '3D': 'Silver Spring',
    '4D': 'Wheaton',
    '5D': 'Germantown',
    '6D': 'Gaithersburg' # Montgomery Village is within Gaithersburg for census purposes
}

df2['city'] = df2['district'].map(district_to_city_map)

print("District to City Mapping created and applied to df2:")
display(df2[['district', 'city']].head())

# 2. Fetch ACS Data for Montgomery County Places (Cities) using requests

# Define the ACS variables we want to fetch
# You can explore the full list at https://api.census.gov/data/2024/acs/acs5/variables.html
acs_variables = {
    'B01003_001E': 'Total Population',
    'B02001_002E': 'White Alone',
    'B02001_003E': 'Black or African American Alone',
    'B02001_004E': 'American Indian and Alaska Native Alone',
    'B02001_005E': 'Asian Alone',
    'B02001_006E': 'Native Hawaiian and Other Pacific Islander Alone',
    'B02001_007E': 'Some Other Race Alone',
    'B03003_003E': 'Hispanic or Latino',
    'B19013_001E': 'Median Household Income',
    'B17001_002E': 'Poverty Status (Below Poverty Level)'
}

# Construct the API URL
# Montgomery County, Maryland: State FIPS 24, County FIPS 031
# Using 2022 5-year estimates as 2024 ACS5 data might not be fully released for 'place' level yet.
# If 2024 is explicitly needed and available, change the 'year' variable.
year = 2022
variables_str = ','.join(acs_variables.keys())
# Corrected URL: Fetch all places in Maryland (state:24) and then filter later
acs_api_url = f"https://api.census.gov/data/{year}/acs/acs5?get=NAME,{variables_str}&for=place:*&in=state:24"

print(f"Fetching data from: {acs_api_url}")

response = requests.get(acs_api_url)
data = response.json()

# The first row contains headers, subsequent rows are data
headers = data[0]
acs_df = pd.DataFrame(data[1:], columns=headers)

# Rename columns for clarity
acs_df = acs_df.rename(columns=acs_variables)

# Extract city name from the 'NAME' column
# Example: 'Gaithersburg city, Maryland' -> 'Gaithersburg'
acs_df['city'] = acs_df['NAME'].apply(lambda x: x.split(',')[0].replace(' city', '').replace(' CDP', '').strip())

# Convert demographic columns to numeric, handling potential non-numeric values
for col in acs_variables.values():
    acs_df[col] = pd.to_numeric(acs_df[col], errors='coerce')


# 3. Merge ACS Data with df2

# Before merging, let's ensure city names match in both dataframes
# The ACS data might have more formal names, let's try to standardize

# Standardize city names in ACS data to match our district map
# For example, 'Gaithersburg city, Maryland' -> 'Gaithersburg'
acs_df['city_standardized'] = acs_df['city'].str.replace(' city', '').str.replace(' CDP', '').str.strip()

# Filter df2 for incidents that have a mapped city
df2_with_city = df2.dropna(subset=['city'])

# Merge df2_with_city with acs_df
# Use a left merge to keep all bias incidents and add ACS data where available
df2_merged = pd.merge(df2_with_city, acs_df, left_on='city', right_on='city_standardized', how='left')

print("\nMerged DataFrame (df2_merged) head:")
display(df2_merged.head())

print("\nInfo on merged DataFrame:")
df2_merged.info()

# Display fetched ACS data head
print("\nFetched ACS Data for Montgomery County Cities:")
display(acs_df)
