from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd 
import zipfile

def download_vikrant_data(output_dir="vikrant_data"):
    api = KaggleApi()
    api.authenticate()

    dataset = "sibichakkaravarthys/vikrant-honeypot-data"

    # Create output directory if doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print("Downloading dataset...")
    # Download dataset zip (this saves as archive.zip by default)
    api.dataset_download_files(dataset, path=output_dir, unzip=False, force=True)

    # List files in output directory to confirm zip presence
    files = os.listdir(output_dir)
    print(f"Files in {output_dir}: {files}")

    # Find the zip file (should be vikrant-honeypot-data.zip or archive.zip)
    zip_files = [f for f in files if f.endswith(".zip")]
    if not zip_files:
        raise FileNotFoundError(f"No .zip files found in {output_dir} after download!")
    
    zip_path = os.path.join(output_dir, zip_files[0])
    print(f"Found zip file: {zip_path}")

    # Extract zip contents
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Extracted all files to {output_dir}")

    # Optional: delete the zip after extraction
    os.remove(zip_path)
    print(f"Removed zip file: {zip_path}")

    return output_dir

if __name__ == "__main__":
    download_vikrant_data()



#EXTRACT CSV'S 










#Transform CSV'S (DATE, LOCATION, SOURCE, )




#lOAD.....

