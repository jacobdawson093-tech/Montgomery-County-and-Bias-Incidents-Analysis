For all coding performed, I use a API link and follow the same procedure of cleaning and ingesting code as shown in the scripts file before anything. 
This is to ensure that future users who test my code will see the most up to date data from the API link.  
**Step 1:** use 'Initial Code and Libraries Used.py' cell  
**Step 2:** use 'Cleaning and preparing Bias Incidents Data.py' cell  
**Step 3:** use 'combing Bias incident with Maryland ACS 5 data.py' cell  
**future users may have to change the app_token in the API link by accessing the MCPD Bias Incidents website (link is in Data folder) and obtaining a new key.**

# MCPD Bias Incidents
* converting 'incident_date' to datetime variable
* Add binary variable for if case is 'resolved' or 'unresolved'
* Convert suspect age to numeric
* Create binary variable for if suspect is under 18 or not
* Add binary variable for if bias was religious or racial

# Combined Data of ACS 5 (2016-2024) and MCPD Bias Incidents
* Change police district to their corresponding city
* Collect demographic data for each city through API link (Up to date)
* Combine MCPD bias incidents with ACS 5 variables grouped by city

# **To reiterate, all analysis, testing, and model creation includes these steps with API links and code to ensure all information is up to date.**  
