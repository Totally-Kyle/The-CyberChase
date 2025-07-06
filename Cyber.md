To better understand patterns in cyberattack activity, our group merged eight CSV files representing daily logs from February 5th to 12th. We added a day column to each file before merging, giving us a clearer, date-specific view of events across the full week. This setup helps us preserve the context of when each log was recorded, making it easier to identify trends over time and will assist in future decisions about which features to keep or drop during modeling.

Each row in the dataset represents a network flow or honeypot event, and each column reflects a specific attribute of that event—like the source/destination IP, protocol, packet counts, and TCP flags. To make the dataset more readable and analysis-friendly, we geotagged both IPs using MaxMind’s GeoLite2 database, adding new columns for location while planning to drop the raw IPs. These transformations help establish relationships between origin, destination, and behavioral traits, laying a foundation for both visualization and potential machine learning tasks.






