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

# 2. Fetch ACS Data for Montgomery County Places (Cities) using requests for multiple years

# Define the ACS variables we want to fetch
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

variables_str = ','.join(acs_variables.keys())

all_acs_dfs = []
# Loop through years from 2016 up to the current year (to capture the latest available ACS 5-year estimates)
# ACS 5-year estimates for year Y are typically released in December of year Y+1. So, requesting up to the current year
# will ensure we get the latest published data without trying to fetch future, unavailable data.
for current_year in range(2016, datetime.datetime.now().year):
    acs_api_url = f"https://api.census.gov/data/{current_year}/acs/acs5?get=NAME,{variables_str}&for=place:*&in=state:24"
    print(f"Fetching data from: {acs_api_url}")

    try:
        response = requests.get(acs_api_url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # The first row contains headers, subsequent rows are data
        headers = data[0]
        temp_acs_df = pd.DataFrame(data[1:], columns=headers)

        # Rename columns for clarity
        temp_acs_df = temp_acs_df.rename(columns=acs_variables)

        # Extract city name from the 'NAME' column
        temp_acs_df['city'] = temp_acs_df['NAME'].apply(lambda x: x.split(',')[0].replace(' city', '').replace(' CDP', '').strip())

        # Convert demographic columns to numeric, handling potential non-numeric values
        for col in acs_variables.values():
            temp_acs_df[col] = pd.to_numeric(temp_acs_df[col], errors='coerce')

        # Add a year column to identify the ACS 5-year estimate
        temp_acs_df['acs_year_end'] = current_year
        all_acs_dfs.append(temp_acs_df)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {current_year}: {e}")
        # Print response content if available for more debugging info
        if response is not None:
            print(f"Response content: {response.text}")
        continue # Skip to the next year
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError for {current_year}: {e}")
        # Print response content if available for more debugging info
        if response is not None:
            print(f"Response content: {response.text}")
        continue # Skip to the next year

# Concatenate all ACS dataframes
acs_df = pd.concat(all_acs_dfs, ignore_index=True)

# 3. Merge ACS Data with df2

# Standardize city names in ACS data to match our district map
acs_df['city_standardized'] = acs_df['city'].str.replace(' city', '').str.replace(' CDP', '').str.strip()

# Filter df2 for incidents that have a mapped city and are within the ACS data range (up to current year)
df2_filtered = df2.dropna(subset=['city']).copy()
df2_filtered = df2_filtered[df2_filtered['incident_date'].dt.year < datetime.datetime.now().year]

# Extract the year from the incident date for merging
df2_filtered['incident_year'] = df2_filtered['incident_date'].dt.year

# Merge df2_filtered with acs_df
# Use a left merge to keep all filtered bias incidents and add ACS data where available
df2_merged = pd.merge(df2_filtered, acs_df,
                      left_on=['city', 'incident_year'],
                      right_on=['city_standardized', 'acs_year_end'],
                      how='left')

print("\nMerged DataFrame (df2_merged) head:")
display(df2_merged.head())

print("\nInfo on merged DataFrame:")
df2_merged.info()

# Display fetched ACS data head
print("\nFetched and Combined ACS Data for Montgomery County Cities (multiple years):")
display(acs_df.head())
print("\nInfo on Combined ACS DataFrame:")
acs_df.info()
