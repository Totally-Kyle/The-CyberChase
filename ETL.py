import pandas as pd
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import requests
import shutil
import geoip2.database


# === Step 1: Authenticate with Kaggle API ===
api = KaggleApi()
api.authenticate()

# === Step 2: Dataset info ===
dataset = 'sibichakkaravarthys/vikrant-honeypot-data'
download_dir = 'tmp_download'
zip_path = os.path.join(download_dir, 'vikrant-honeypot-data.zip')
target_subfolder = 'csv-daily-data-20230612T101401Z-001/csv-daily-data'
output_dir = 'DATA'

# === Step 3: Create necessary folders ===
os.makedirs(download_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# === Step 4: Download dataset ===
print("📥 Downloading dataset from Kaggle...")
api.dataset_download_files(dataset, path=download_dir, unzip=False)
print("✅ Download complete.")

# === Step 5: Extract and flatten only the target subfolder ===
print(f"📦 Extracting and flattening: {target_subfolder}/ → {output_dir}/")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for member in zip_ref.namelist():
        if member.startswith(target_subfolder + '/') and not member.endswith('/'):
            # Flatten path: just get the filename (e.g. 2023-02-05.csv)
            filename = os.path.basename(member)
            target_path = os.path.join(output_dir, filename)

            # Extract file
            with zip_ref.open(member) as source, open(target_path, "wb") as target:
                shutil.copyfileobj(source, target)
            print(f"✓ Extracted: {filename}")

# === Step 6: Cleanup ===
os.remove(zip_path)
shutil.rmtree(download_dir)
print("\n✅ All .csv files extracted to 'DATA/' and temporary files cleaned up.")

# === Step 7: Read-In ===
import os
import pandas as pd

# Base directory for input and output
base_dir = os.path.join(os.path.dirname(__file__), 'DATA')

# File names and corresponding days
file_info = [
    ('2023-02-05.csv', 5),
    ('2023-02-06.csv', 6),
    ('2023-02-07.csv', 7),
    ('2023-02-08.csv', 8),
    ('2023-02-09.csv', 9),
    ('2023-02-10.csv', 10),
    ('2023-02-11.csv', 11),
    ('2023-02-12.csv', 12)
]

# Read and tag each file
dfs = []
for filename, day in file_info:
    file_path = os.path.join(base_dir, filename)
    df = pd.read_csv(file_path)
    df['day'] = day
    dfs.append(df)

# Merge into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save merged CSV into the same DATA folder
output_path = os.path.join(base_dir, 'feb5-12_merged.csv')
merged_df.to_csv(output_path, index=False)

print(f"✅ Merged CSV saved to: {output_path}")

# === Step 8: TRANSFORM ===
# Download IP-Location database
# Target download URL (git.io shortlink)
url = 'https://git.io/GeoLite2-City.mmdb'

# Destination directory and file path
data_dir = os.path.join(os.path.dirname(__file__), 'DATA')
os.makedirs(data_dir, exist_ok=True)  # Ensure DATA folder exists

mmdb_path = os.path.join(data_dir, 'GeoLite2-City.mmdb')

# Download the file
print("📥 Downloading GeoLite2-City.mmdb...")
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(mmdb_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"✅ File saved to: {mmdb_path}")
else:
    print(f"❌ Failed to download file. Status code: {response.status_code}")

reader = geoip2.database.Reader('/Users/sa12/Documents/Repositories/The-CyberChase/DATA/GeoLite2-City.mmdb')
# Build location info
locations = []

for ip in merged_df['Src IP']:
    try:
        response = reader.city(ip)
        country = response.country.name or "Unknown Country"
        city = response.city.name or "Unknown City"

        location_str = f"{country}"
    except Exception as e:
        location_str = f"Error: {e}"

    locations.append(location_str)

# Add to DataFrame
merged_df['Location'] = locations
print(merged_df)