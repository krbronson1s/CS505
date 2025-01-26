import zipfile
import os
import requests

def download_and_extract_zip(url, extract_to):
    # Step 1: Download the ZIP file
    zip_filename = 'kagglecatsanddogs_5340.zip'
    zip_file_path = os.path.join(extract_to, zip_filename)

    print(f"Downloading {url}...")
    response = requests.get(url)
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded ZIP file to {zip_file_path}")

    # Step 2: Extract the ZIP file
    print(f"Extracting ZIP file to {extract_to}...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted files to {extract_to}")

def get_image_paths(extracted_dir):
    # List all image files in the extracted directory
    image_files = [os.path.join(extracted_dir, file) for file in os.listdir(extracted_dir) if file.endswith(('jpg', 'png'))]
    return image_files

if __name__ == "__main__":
    url = 'https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip'
    extraction_dir = 'images/'  # Folder where images will be extracted

    # Create directory if it doesn't exist
    if not os.path.exists(extraction_dir):
        os.makedirs(extraction_dir)

    # Download and extract the ZIP file
    download_and_extract_zip(url, extraction_dir)

    # Get the list of image paths
    image_paths = get_image_paths(extraction_dir)
    print("Extracted image paths:", image_paths)

    # Save the image paths to notes.txt (if needed)
    with open('notes.txt', 'w') as file:
        for path in image_paths:
            file.write(f"{path}\n")
