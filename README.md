![screenshots](images/JackBreacher.png)

# Welcome to project Jack Breacher 

Cyberattacks aren’t just rising — they’re evolving. Every day, thousands of intrusion attempts target systems around the world, growing more complex and harder to detect. As more organizations shift their operations to the cloud, staying ahead of these threats has never been more important.

In this project, we dig into real honeypot data to better understand attacker behavior. Where are most of the attempts coming from? When do they happen? And what signs can help us catch them before they succeed? By combining data analysis, geolocation, and machine learning, we uncover patterns that can help teams strengthen their defenses and stay one step ahead.


## Modules/Libaries 
* Pandas
* Seaborn
* Numpy
* MatplotLib
* Scikit-learn
* geoip2.database

## Dataset

The data was sourced from honeypot sensors deployed globally, capturing intrusion attempts including metadata such as:

* Source IP & geolocation
* Honeypot type targeted (e.g., ddospot, adbhoney, redispot)
* Timestamp of attempt
* Protocol and traffic metadata

## Objectives 

* Identify top countries originating attacks
* Determine the most common attack types
* Analyze temporal attack patterns by day and hour
* Use geolocation and visualization to map threat landscapes
* Explore machine learning methods for pattern recognition

## Methodology 
1. Data Collection:
  * Obtained from honeypot logs covering 7 consecutive days.
  * Mapped IP addresses to geolocation using geoip2.database.

2. Data Cleaning & Processing:
  * Removed incomplete and duplicate entries.
  * Converted timestamps to EST for temporal analysis.

3. Analysis & Visualization:
  * Used pandas, numpy, and matplotlib/seaborn for analysis.
  * Created bar charts, treemaps, and time series visualizations to answer key questions.

4. Machine Learning:
  * Applied exploratory clustering to detect attack pattern similarities.

## Key Findings 

* Concentration of Sources:
  * Iran: 533,013 attacks.
  * United States: 362,552 attacks.

* Top 10 countries accounted for over 1.5 million attacks.
  *![Placeholder for Top 10 Countries Bar Chart]

Attack Types:
  * Most frequent: ddospot, adbhoney, and redispot.
![Placeholder for Attack Type Treemap]

* Temporal Patterns:
  * Peak days: Tuesday and Thursday.
  * Peak hours: 1 AM – 9 AM EST.
![Placeholder for Hourly Attack Trends Chart]

*Unexpected Findings:
High attack volume originating from U.S. infrastructure suggests compromised domestic servers or proxy usage.

## Future Work
* Expand machine learning models for real-time attack prediction.
* Integrate with SIEM platforms for live monitoring.
* Broaden dataset to cover multiple months for seasonal pattern analysis.

## Contributors
Krystel Carrera Reyes
Garry Clark
Kyle Miller
Elorna Pierre
Jonathan Slater