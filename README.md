# Ithmb2Jpg Converter

This Python script is designed to convert `.ithmb` files (iPod photo cache files) into `.jpg` image files. It allows users to specify input and output directories, validates `.ithmb` files, extracts images, and logs the conversion process.

## Features

- **Dynamic Input/Output:** Prompts the user to specify the input folder containing `.ithmb` files and the output folder for `.jpg` images.
- **File Validation:** Ensures `.ithmb` files can be processed before attempting conversion.
- **Parallel Processing:** Utilizes multiple CPU cores for faster conversions.
- **Detailed Logging:** Tracks successfully converted files and logs errors encountered during the process.
- **Progress Feedback:** Displays progress bars for file validation and image extraction using the `tqdm` library.

## Prerequisites

Before running the script, ensure the following dependencies are installed:

- Python 3.6 or higher
- `ithmbconverter` library (required for `.ithmb` file handling)
- `tqdm` library (for progress bars)

You can install the required dependencies using pip:

```bash
pip install tqdm ithmbconverter
```

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script:

```bash
python ithmb2jpg.py
```

4. Enter the required directories when prompted:
    - **Input Directory:** The folder containing `.ithmb` files.
    - **Output Directory:** The folder where the converted `.jpg` images will be saved.

## Example

```text
Enter the path to the folder containing .ithmb files: /path/to/ithmb/files
Enter the path to the output folder: /path/to/output
Found 10 .ithmb files.
[Progress bars for validation and conversion]
Conversion summary:
Successfully converted: 8 files
  - file1.ithmb: 20 images
  - file2.ithmb: 15 images
Error summary:
Invalid file structure: 2 occurrences
  - file9.ithmb
  - file10.ithmb
```

## How It Works

1. **Input/Output Directories:**
   - The script prompts the user to input the paths to the directories for processing and saving files.
2. **File Scanning:**
   - Recursively scans the input directory for `.ithmb` files.
3. **Validation:**
   - Uses `ITHMBConverter` to check if files can be processed.
4. **Image Extraction:**
   - Extracts images from valid `.ithmb` files and saves them as `.jpg` files in the output directory.
5. **Logging:**
   - Keeps track of successful conversions and logs errors for troubleshooting.

## Output Structure

The converted `.jpg` files will be saved in the specified output directory with filenames in the format:

```
<original_filename>_image_<index>.jpg
```

## Error Handling

- **Invalid File Structure:** Files that fail validation are logged.
- **Save Errors:** Issues during image saving (e.g., write permissions) are also logged.

## Limitations

- Requires the `ithmbconverter` library, which must be installed separately.
- Assumes `.ithmb` files are stored in a single root directory or its subdirectories.

## License

This script is provided "as-is" under the MIT License. Feel free to modify and distribute it as needed.

---

Enjoy converting your `.ithmb` files into accessible `.jpg` images!
