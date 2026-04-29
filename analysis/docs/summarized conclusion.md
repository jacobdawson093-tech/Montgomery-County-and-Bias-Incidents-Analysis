The following is summarized findings of tests and analysis, using data from ingestion steps. This information is as of April of 2026, but is subject to change in the future. To see up to date analysis, p-values, Chi2 values, coefficiants, and more; open the notebook and run it yourself which uses the up to date API. 

# Summary of Key Findings and Statistical Tests

This analysis investigated various aspects of bias incidents, their resolution rates, demographic factors, and suspect characteristics.

## 1. Z-test for Resolution Rates: Religious vs. Racial/Ethnic Biases
*   **Purpose**: To determine if there's a statistically significant difference in resolution rates between religious and racial/ethnic bias incidents.
*   **Methodology**: Two-sample z-test for proportions, comparing resolution rates of 'Religious Bias' vs. 'Racial/Ethnic Bias' categories.
*   **Finding**: There is a **statistically significant difference** (Z-statistic: -1.98, P-value: 0.0479). Racial bias incidents (40.81% resolved) are **more likely to be resolved** than religious bias incidents (36.22% resolved).

## 2. Chi-square Test (Fisher's Exact Test) for Religious Bias Groups vs. Resolution
*   **Purpose**: To examine if specific religious bias types (grouped) are associated with their likelihood of being resolved.
*   **Methodology**: Fisher's Exact Test applied to a contingency table of grouped religious bias types ('Anti-Jewish' vs. 'Minor Religious Biases') and resolution status.
*   **Finding**: There is **no statistically significant association** (P-value: 0.2246). The likelihood of resolution does not significantly differ between Anti-Jewish incidents and other grouped religious biases.

## 3. Chi-square Tests for Racial/Ethnic Bias Groups vs. Resolution

### a) Including 'Anti-American Indian' (with caution)
*   **Purpose**: To test for an association between specific racial/ethnic bias types (including all observed, even low counts) and resolution status.
*   **Methodology**: Chi-square test of independence.
*   **Finding**: A **statistically significant association** was found (Chi2: 24.93, P-value: 0.0004). However, this finding was noted with **caution** due to 'Anti-American Indian' having very low counts, violating chi-square assumptions.

### b) Excluding 'Anti-American Indian' (robust finding)
*   **Purpose**: To re-evaluate the association between racial/ethnic bias types and resolution status after removing categories with insufficient data (e.g., 'Anti-American Indian').
*   **Methodology**: Chi-square test of independence on filtered data.
*   **Finding**: A **statistically significant association** remains (Chi2: 24.82, P-value: 0.0002). This finding is considered **robust** as it satisfies the test's assumptions, indicating that the specific type of racial/ethnic bias significantly impacts whether an incident is resolved.

## 4. Z-test for Under-18 Suspects in Bias Incidents
*   **Purpose**: To determine if individuals under 18 years old are disproportionately represented as suspects in bias incidents.
*   **Methodology**: One-sample proportions z-test, comparing the observed proportion of under-18 suspects to a null hypothesis of 50%.
*   **Finding**: The test showed a **statistically significant result** (Z-statistic: 10.67, P-value: 0.0000). Individuals below the age of 18 are **disproportionately more likely** to be suspects in bias incidents (65.23% of known-age suspects).

## 5. Pearson's Correlation: Population & Income vs. Average Annual Bias Incidents
*   **Purpose**: To examine the linear relationship between city-level demographics (total population, median household income) and the average annual number of bias incidents.
*   **Methodology**: Pearson's correlation coefficient test.
*   **Finding**: 
    *   **Median Household Income**: No statistically significant linear association (Pearson Corr: 0.81, P-value: 0.0518).
    *   **Total Population**: No statistically significant linear association (Pearson Corr: -0.45, P-value: 0.3694).

## 6. ANOVA: Mean Annual Bias Incidents Between Cities
*   **Purpose**: To determine if there are statistically significant differences in the mean annual bias incidents across different cities.
*   **Methodology**: One-Way ANOVA.
*   **Finding**: There is **no statistically significant difference** in the mean annual bias incidents between cities (F-statistic: 2.01, P-value: 0.0942). The observed variations are likely due to random chance.

## 7. Pearson's Correlation: Resolution Rate vs. Racial Population Proportion

### a) Using Yearly Data (Yearly Resolution Rate vs. Yearly Population Proportion)
*   **Purpose**: To find if there's a linear correlation between the yearly resolution rate for specific racial bias types and the yearly population proportion of the corresponding racial group in a city.
*   **Methodology**: Pearson's correlation coefficient test for each racial bias type (Anti-Black, Anti-White, Anti-Asian, Anti-Hispanic) over all years and cities.
*   **Finding**: **No statistically significant correlation** was found for any of the tested racial bias types (Anti-Black P-value: 0.18, Anti-White P-value: 0.65, Anti-Asian P-value: 0.54, Anti-Hispanic P-value: 0.32).

### b) Using Averaged Data (Average Resolution Rate vs. Average Population Proportion)
*   **Purpose**: To find if there's a linear correlation between the *average* resolution rate for specific racial bias types and the *average* population proportion of the corresponding racial group in a city.
*   **Methodology**: Pearson's correlation coefficient test for each racial bias type using averaged data across years.
*   **Finding**: 
    *   For **Anti-Black** incidents, there was a **statistically significant positive correlation** (Pearson Corr: 0.86, P-value: 0.0271) between the average resolution rate and the average Black or African American Alone Proportion in cities.
    *   For Anti-White, Anti-Asian, and Anti-Hispanic incidents, **no statistically significant correlation** was found with their respective average population proportions.

--- 
