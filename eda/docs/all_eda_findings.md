**The following is using the MCPD Bias Incident data set from years 2016-2026. What is displayed is summary statistics as of April of 2026. Future data will be added and these summary statistics therefore will not be the same.**
**To see the up to date statistics, go to notebooks and EDA to see most up to date information using API link.**

**Furthermore, EDA is using raw data of only the MCPD Bias Incidents dataset using up to date API link, ingestion steps are not used.**

# Consolidated EDA Statistical Findings

## Status Distribution

| status           |   Count |   Percentage |
|:-----------------|--------:|-------------:|
| Open             |    1017 |    46.5873   |
| Closed-Admin     |     673 |    30.8291   |
|                  |     191 |     8.74943  |
| Closed-Arrest    |     123 |     5.63445  |
| Inactive         |      94 |     4.306    |
| Closed-Exception |      43 |     1.96977  |
| UNF              |      29 |     1.32845  |
| RTOJ             |       8 |     0.366468 |
|                  |       5 |     0.229043 |

## Incidents Per Month

|   Month |   Incident Count |
|--------:|-----------------:|
|       1 |              174 |
|       2 |              229 |
|       3 |              235 |
|       4 |              181 |
|       5 |              212 |
|       6 |              183 |
|       7 |              107 |
|       8 |              128 |
|       9 |              173 |
|      10 |              194 |
|      11 |              201 |
|      12 |              166 |

## Victim Type Distribution

| victim_type                    |   Count |   Percentage |
|:-------------------------------|--------:|-------------:|
| Individual(s)                  |    1186 |    54.3289   |
| School/College                 |     553 |    25.3321   |
| Society                        |     164 |     7.5126   |
| Religious Organization         |     129 |     5.9093   |
| Business/Financial Institution |      91 |     4.16858  |
| Government                     |      27 |     1.23683  |
| Other                          |      19 |     0.870362 |
|                                |      14 |     0.641319 |

## District Distribution

| district   |   Count |   Percentage |
|:-----------|--------:|-------------:|
| 2D         |     565 |     25.8818  |
| 4D         |     383 |     17.5447  |
| 1D         |     303 |     13.88    |
| 5D         |     268 |     12.2767  |
| 3D         |     244 |     11.1773  |
| 6D         |     177 |      8.10811 |
| RCPD       |     116 |      5.31379 |
| GCPD       |     101 |      4.62666 |
| TPPD       |      26 |      1.19102 |

## Numerical Summary

| Unnamed: 0   |   no_of_victims |   no_of_suspects |   suspects_less_than_18_years |   suspects_18_35_years_old |   suspects_36_45_years_old |   suspects_46_55_years_old |   suspects_55_years_old |
|:-------------|----------------:|-----------------:|------------------------------:|---------------------------:|---------------------------:|---------------------------:|------------------------:|
| count        |     1188        |      1185        |                    552        |                 131        |                  86        |                  66        |               83        |
| mean         |        1.25253  |         1.28692  |                      1.31522  |                   1.09924  |                   1.03488  |                   1.0303   |                1.03614  |
| std          |        0.732126 |         0.784374 |                      0.831713 |                   0.324748 |                   0.184561 |                   0.172733 |                0.187784 |
| min          |        1        |         1        |                      1        |                   1        |                   1        |                   1        |                1        |
| 25%          |        1        |         1        |                      1        |                   1        |                   1        |                   1        |                1        |
| 50%          |        1        |         1        |                      1        |                   1        |                   1        |                   1        |                1        |
| 75%          |        1        |         1        |                      1        |                   1        |                   1        |                   1        |                1        |
| max          |       11        |        10        |                      9        |                   3        |                   2        |                   2        |                2        |

## Initial Data Head

|        id | incident_date   | district   | bias_code   | bias                               | status       | victim_type    |   no_of_victims |   no_of_suspects |   suspects_36_45_years_old |   suspects_55_years_old | unknown   |   suspects_less_than_18_years | bias_code_2   | suspects_18_35_years_old   | suspects_46_55_years_old   |   incident_year |   incident_month |
|----------:|:----------------|:-----------|:------------|:-----------------------------------|:-------------|:---------------|----------------:|-----------------:|---------------------------:|------------------------:|:----------|------------------------------:|:--------------|:---------------------------|:---------------------------|----------------:|-----------------:|
| 260013584 | 2026-03-31      | 6D         | Anti-Jewish | Vandalism                          | Closed-Admin | School/College |             nan |              nan |                        nan |                     nan |           |                           nan |               |                            |                            |            2026 |                3 |
| 260013065 | 2026-03-27      | 5D         | Anti-Black  | Vandalism                          | Closed-Admin | School/College |             nan |              nan |                        nan |                     nan |           |                           nan |               |                            |                            |            2026 |                3 |
| 260013221 | 2026-03-27      | 4D         | Anti-Jewish | Assault (simple)                   | Open         | Individual(s)  |               2 |                2 |                          1 |                       1 | Known     |                           nan |               |                            |                            |            2026 |                3 |
| 260012859 | 2026-03-25      | 2D         | Anti-Jewish | Vandalism                          | Open         | Society        |             nan |              nan |                        nan |                     nan |           |                           nan |               |                            |                            |            2026 |                3 |
| 260012953 | 2026-03-25      | 5D         | Anti-Black  | Verbal Intimidation/Simple Assault | Open         | Individual(s)  |               2 |                2 |                        nan |                     nan | Known     |                             1 |               |                            |                            |            2026 |                3 |

## Incidents Per Year

|   Year |   Incident Count |
|-------:|-----------------:|
|   2016 |               98 |
|   2017 |              122 |
|   2018 |               93 |
|   2019 |              114 |
|   2020 |              117 |
|   2021 |              144 |
|   2022 |              160 |
|   2023 |              466 |
|   2024 |              485 |
|   2025 |              332 |
|   2026 |               52 |

## Bias Code 2 Distribution

| bias_code_2                |   Count |   Percentage |
|:---------------------------|--------:|-------------:|
|                            |    1977 |   90.5634    |
| Anti-Black                 |      65 |    2.97755   |
| Anti-Jewish                |      45 |    2.06138   |
| Anti-Homosexual            |      37 |    1.69492   |
| Anti-Hispanic              |      17 |    0.778745  |
| Anti-Multi-Religious Group |       7 |    0.32066   |
| Anti-Multi-Racial          |       7 |    0.32066   |
| Anti-Transgender           |       6 |    0.274851  |
| Anti-Mental Disability     |       4 |    0.183234  |
| Anti-Male Homosexual       |       4 |    0.183234  |
| Anti-Asian                 |       3 |    0.137426  |
| Anti-Islamic               |       3 |    0.137426  |
| Anti-Other Religion        |       2 |    0.091617  |
| Anti-Other Ethnicity       |       2 |    0.091617  |
| Anti-Bisexual              |       2 |    0.091617  |
| Anti-Gender Non-Conforming |       1 |    0.0458085 |
| Anti-White                 |       1 |    0.0458085 |

## Bias Code Distribution

| bias_code                  |   Count |   Percentage |
|:---------------------------|--------:|-------------:|
| Anti-Jewish                |     766 |   35.0893    |
| Anti-Black                 |     695 |   31.8369    |
| Anti-Homosexual            |     154 |    7.05451   |
| Anti-Asian                 |     105 |    4.80989   |
| Anti-Hispanic              |      98 |    4.48923   |
| Anti-Multi-Racial          |      66 |    3.02336   |
| Anti-Islamic               |      60 |    2.74851   |
| Anti-White                 |      46 |    2.10719   |
| Anti-Male Homosexual       |      44 |    2.01557   |
| Anti-Transgender           |      40 |    1.83234   |
| Anti-Other Ethnicity       |      22 |    1.00779   |
| Anti-Arab                  |      11 |    0.503894  |
| Anti-Mental Disability     |      10 |    0.458085  |
| Anti-Catholic              |      10 |    0.458085  |
| Anti-Female Homosexual     |       9 |    0.412277  |
| Anti-Multi-Religious Group |       7 |    0.32066   |
| Anti-Other Religion        |       7 |    0.32066   |
|                            |       6 |    0.274851  |
| Anti-Gender Non-Conforming |       6 |    0.274851  |
| Anti-Other Christian       |       6 |    0.274851  |
| Anti-Physical Disability   |       3 |    0.137426  |
| Anti-Hindhu                |       3 |    0.137426  |
| Anti-Protestant            |       2 |    0.091617  |
| Anti-Buddhist              |       2 |    0.091617  |
| Anti-American Indian       |       2 |    0.091617  |
| Anti-Female                |       1 |    0.0458085 |
| Anti-Heterosexual          |       1 |    0.0458085 |
| Anti-Sikh                  |       1 |    0.0458085 |

## Bias Distribution

| bias                                 |   Count |   Percentage |
|:-------------------------------------|--------:|-------------:|
| Vandalism                            |     807 |    36.9675   |
| Verbal Intimidation/Simple Assault   |     625 |    28.6303   |
| Written Intimidation/Simple Assault  |     269 |    12.3225   |
| Other                                |     173 |     7.92487  |
| Assault (simple)                     |     129 |     5.9093   |
| Social Media                         |      44 |     2.01557  |
| Flyer Left Behind                    |      39 |     1.78653  |
| Physical Intimidation/Simple Assault |      33 |     1.51168  |
| Assault (physical)                   |      25 |     1.14521  |
| Vandalism-Motor Vehicle              |      22 |     1.00779  |
| Display of Noose                     |      11 |     0.503894 |
|                                      |       6 |     0.274851 |

