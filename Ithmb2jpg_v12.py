import os
from ithmbconverter import ITHMBConverter
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from collections import defaultdict

def validate_ithmb_file(ithmb_path):
    try:
        # Check if the file can be processed by ITHMBConverter
        converter = ITHMBConverter(ithmb_path)
        return converter.is_valid()
    except Exception as e:
        print(f"Validation failed for {ithmb_path}: {e}")
    return False

def convert_ithmb_to_images(ithmb_path, output_dir, success_log, error_log):
    try:
        converter = ITHMBConverter(ithmb_path)
        images = converter.extract_images()
        image_count = 0

        for idx, image_data in enumerate(images):
            try:
                output_file = os.path.join(output_dir, f"{os.path.basename(ithmb_path)}_image_{idx}.jpg")
                with open(output_file, "wb") as img_file:
                    img_file.write(image_data)
                image_count += 1
            except Exception as e:
                error_log["Save Error"].append((ithmb_path, idx, str(e)))

        if image_count > 0:
            success_log[ithmb_path] = image_count
    except Exception as e:
        error_log[str(e)].append(ithmb_path)

def scan_and_convert_ithmb():
    # Prompt user for input and output directories
    main_folder = input("Enter the path to the folder containing .ithmb files: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ithmb_files = []
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.lower().endswith(".ithmb"):
                ithmb_files.append(os.path.join(root, file))

    print(f"Found {len(ithmb_files)} .ithmb files.")
    max_threads = os.cpu_count() // 2

    success_log = defaultdict(int)
    error_log = defaultdict(list)

    with ThreadPoolExecutor(max_threads) as executor:
        futures = {}
        for ithmb_path in tqdm(ithmb_files, desc="Validating files"):
            if validate_ithmb_file(ithmb_path):
                futures[executor.submit(convert_ithmb_to_images, ithmb_path, output_folder, success_log, error_log)] = ithmb_path
            else:
                error_log["Invalid file structure"].append(ithmb_path)

        for _ in tqdm(as_completed(futures), total=len(futures), desc="Converting .ithmb files"):
            pass

    print("Conversion summary:")
    print(f"Successfully converted: {len(success_log)} files")
    for file, count in list(success_log.items())[:5]:  # Show up to 5 examples of successful conversions
        print(f"  - {file}: {count} images")

    print("Error summary:")
    for error, files in error_log.items():
        print(f"{error}: {len(files)} occurrences")
        for f in files[:5]:  # Show up to 5 examples per error
            print(f"  - {f}")

if __name__ == "__main__":
    scan_and_convert_ithmb()
