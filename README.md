# Ithmb2Jpg Converter

This Python script extracts and converts `.ithmb` files (iPod photo cache files) into `.jpg` image files. It allows users to specify input and output directories, scans `.ithmb` files for embedded JPEG images, and logs the conversion process.

## Features

- **Dynamic Input/Output:** Prompts the user to specify the input folder containing `.ithmb` files and the output folder for `.jpg` images.
- **JPEG Extraction:** Detects and extracts valid JPEG images from `.ithmb` files instead of assuming a raw format.
- **Parallel Processing:** Utilizes multiple CPU cores for faster conversions.
- **Automatic Corruption Check:** Deletes corrupted or unreadable `.jpg` files after extraction.
- **Detailed Logging:** Tracks successfully converted files and logs errors encountered during the process.
- **Progress Feedback:** Displays progress bars for file scanning and image extraction using the `tqdm` library.

## Prerequisites

Before running the script, ensure the following dependencies are installed:

- Python 3.6 or higher
- `opencv-python` (for image validation)
- `tqdm` (for progress bars)
- `icecream` (for debugging)

You can install the required dependencies using pip:

```bash
pip install tqdm opencv-python icecream
```

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script:

```bash
python ithmb_converter.py
```

4. Enter the required directories when prompted:
    - **Input Directory:** The folder containing `.ithmb` files.
    - **Output Directory:** The folder where the converted `.jpg` images will be saved.

## Example

```text
Enter the path to the folder containing .ithmb files: /path/to/ithmb/files
Enter the path to the output folder: /path/to/output
Found 10 .ithmb files.
[Progress bars for scanning and conversion]
Conversion summary:
Successfully converted: 8 files
  - file1.ithmb: 20 images
  - file2.ithmb: 15 images
Error summary:
No JPEG found: 2 occurrences
  - file9.ithmb
  - file10.ithmb
```

## How It Works

1. **Input/Output Directories:**
   - The script prompts the user to input the paths to the directories for processing and saving files.
2. **File Scanning:**
   - Recursively scans the input directory for `.ithmb` files.
3. **JPEG Extraction:**
   - Scans `.ithmb` files for embedded JPEG images and extracts them.
4. **Image Validation:**
   - Uses OpenCV to verify extracted images and delete corrupted files.
5. **Logging:**
   - Keeps track of successful conversions and logs errors for troubleshooting.

## Output Structure

The converted `.jpg` files will be saved in the specified output directory with filenames in the format:

```
<original_filename>_image_<index>.jpg
```

## Error Handling

- **No JPEG Found:** If an `.ithmb` file does not contain valid JPEGs, it is logged.
- **Corrupt Image Removal:** Extracted JPEGs that fail validation are automatically deleted.
- **Permissions Issues:** If the script cannot write to the output folder, it logs the error.

## Limitations

- The script assumes `.ithmb` files contain embedded JPEG images.
- If a different encoding is used, the script may not work correctly.

## License

This script is provided "as-is" under the MIT License. Feel free to modify and distribute it as needed.

---

Enjoy converting your `.ithmb` files into accessible `.jpg` images!

