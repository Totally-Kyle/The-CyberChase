# **Honeypot Cybersecurity Data**
- This Jupyter Notebook performs Exploratory Data Analysis (EDA) on cybersecurity data collected from honeypots for February 12, 2023. The analysis focuses on understanding the dataset, identifying patterns, correlations, and anomalies, and preparing the data for further analysis or modeling.

### **Key Sections and Operations**

#### **1. Importing Libraries**
- Libraries used: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, and `geoip2.database`.
- These libraries are essential for data manipulation, visualization, and geolocation analysis.


#### **2. Loading Data**
- Multiple CSV files for daily honeypot data (February 5–12, 2023) are loaded into separate DataFrames.
- The primary focus for thid EDA is on the dataset for **February 12, 2023** (`Feb12`), which contains **84 columns** and **76,303 rows**.


#### **3. Dataset Overview**
- **`Feb12.info()`**: Provides details about column names, data types, and non-null counts.
- **`Feb12.describe()`**: Summarizes statistical metrics for numerical columns.
- **`Feb12.head()`**: Displays the first few rows of the dataset.


#### **4. Attack Type Analysis**
- The `Label` column categorizes intrusion types (e.g., `ddospot`, `cowrie`, `log4pot`).
  - `ddospot` dominates with over **70,000 detections**.
  - Other attack types (e.g., `cowrie`, `log4pot`) have significantly fewer detections.


#### **5. Protocol Distribution**
- The `Protocol` column is analyzed to understand network protocol usage.

  - Protocol `17` (likely UDP) accounts for **95% of all traffic**.
  - Protocol `6` (likely TCP) has only about **4,000 connections**.



#### **6. Destination Port Analysis**
- The `Dst Port` column is analyzed to identify the **Top 10 Targeted Ports**.
  - Port `123` (likely NTP) is the most targeted, with over **70,000 attempts**.
  - Other ports have significantly fewer attempts.



#### **7. Geolocation Analysis**
- The `Src IP` column is used to determine the geographic locations of source IPs using the **GeoLite2 database**.
  - Locations are added to the dataset in a new column (`Location`).
  - Errors in geolocation are handled gracefully.


#### **9. Feature Selection**
- **Top Features by Variance**:
  - The top 30 features with the highest variance are selected for further analysis.
- **Selected Features**:
  - Includes metrics like `Flow Duration`, `Flow Bytes/s`, `Packet Length Mean`, `SYN Flag Count`, and `Active Mean`.


#### **10. Univariate Analysis**
- **Histograms and Boxplots**:
  - Generated for all numerical columns to understand distributions and detect outliers.
  - Focused on features like `Flow Duration`, `Total Fwd Packet`, and `Packet Length Mean`.



### **Key Insights**
1. **Attack Trends**:
   - `ddospot` attacks dominate the dataset, indicating a focus on Distributed Denial-of-Service (DDoS) activity.
2. **Protocol Usage**:
   - UDP traffic (Protocol `17`) is overwhelmingly dominant, suggesting potential vulnerabilities in UDP-based services.
3. **Targeted Ports**:
   - Port `123` (NTP) is heavily targeted, highlighting the need for securing time synchronization services.
4. **Geolocation**:
   - Source IPs are mapped to geographic locations, providing insights into attack origins.
5. **Feature Correlations**:
   - Strong correlations between certain features (e.g., `Flow Bytes/s` and `Flow Packets/s`) suggest redundancy, which can be addressed during feature selection.

### **What's Next?**
- **Correlation Heatmaps**:
  - Various feature groups (e.g., flow stats, packet length metrics, inter-arrival times, TCP flags) analyzed for correlations.
  - Heatmaps visually highlight strong positive and negative correlations.


### **Conclusion**
This notebook provides a comprehensive analysis of honeypot data for February 12, 2023. It identifies key attack patterns, protocol usage, targeted ports, and correlations between features. The insights gained can be used to enhance network security measures, optimize intrusion detection systems, and prepare the data for machine learning models.