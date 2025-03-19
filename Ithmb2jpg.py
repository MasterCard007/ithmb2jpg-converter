import os
import struct
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import cv2
from collections import defaultdict
from icecream import ic

def extract_jpeg_images(ithmb_file, output_folder):
    """Scans the .ithmb file for embedded JPEG images and extracts them."""
    ic(f"Scanning {ithmb_file} for JPEG signatures")
    try:
        with open(ithmb_file, "rb") as f:
            data = f.read()

        start_marker = b"\xFF\xD8\xFF"  # JPEG start
        end_marker = b"\xFF\xD9"  # JPEG end
        pos = 0
        extracted_files = []

        while True:
            start = data.find(start_marker, pos)
            if start == -1:
                break  # No more JPEGs found
            end = data.find(end_marker, start) + 2
            if end == 1:
                break  # No valid end marker found
            
            jpg_data = data[start:end]
            img_path = os.path.join(output_folder, f"{os.path.basename(ithmb_file)}_image_{len(extracted_files)}.jpg")
            
            with open(img_path, "wb") as img_file:
                img_file.write(jpg_data)
            extracted_files.append(img_path)
            pos = end  # Move to next possible image
            
        return extracted_files
    except Exception as e:
        ic(e)
        return str(e)

def validate_jpeg(file_path):
    """Checks if a JPEG file is valid and not corrupted."""
    try:
        img = cv2.imread(file_path)
        if img is None:
            os.remove(file_path)
            ic(f"Deleted corrupted file: {file_path}")
            return False
        return True
    except Exception as e:
        ic(f"Error validating {file_path}: {e}")
        os.remove(file_path)
        return False

def convert_ithmb_to_images(ithmb_path, output_dir, success_log, error_log):
    ic(f"Extracting JPEGs from {ithmb_path}")
    try:
        extracted_images = extract_jpeg_images(ithmb_path, output_dir)
        if not extracted_images:
            error_log["No JPEG found"].append(ithmb_path)
            return
        
        valid_images = [img for img in extracted_images if validate_jpeg(img)]
        success_log[ithmb_path] = len(valid_images)
    except Exception as e:
        ic(e)
        error_log[str(e)].append(ithmb_path)

def scan_and_convert_ithmb():
    main_folder = input("Enter the path to the folder containing .ithmb files: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()
    ic(main_folder, output_folder)
    
    if not os.path.exists(main_folder):
        print("Error: The input folder does not exist.")
        return
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    ithmb_files = []
    for root, _, files in os.walk(main_folder):
        ic(root, files)
        for file in files:
            if file.lower().endswith(".ithmb"):
                ithmb_files.append(os.path.join(root, file))

    ic(ithmb_files)
    print(f"Found {len(ithmb_files)} .ithmb files.")
    max_threads = os.cpu_count() // 2

    success_log = defaultdict(int)
    error_log = defaultdict(list)

    with ThreadPoolExecutor(max_threads) as executor:
        futures = {executor.submit(convert_ithmb_to_images, ithmb_path, output_folder, success_log, error_log): ithmb_path for ithmb_path in tqdm(ithmb_files, desc="Processing .ithmb files")}
        for _ in tqdm(as_completed(futures), total=len(futures), desc="Finalizing Conversion"):
            pass

    print("\nConversion Summary:")
    print(f"Successfully converted: {len(success_log)} files")
    for file, count in list(success_log.items())[:5]:
        print(f"  - {file}: {count} images")

    print("\nError Summary:")
    for error, files in error_log.items():
        print(f"{error}: {len(files)} occurrences")
        for f in files[:5]:
            print(f"  - {f}")

if __name__ == "__main__":
    scan_and_convert_ithmb()
