import os
import logging
from zipfile import ZipFile
from pathlib import Path

def extract_raw_to_staging(input_dir: str, output_dir: str, pattern: str = '*.zip'):

    logging.info(" STEP: EXTRACT RAW FILES TO STAGING\n")
    
    # List of files
    files = list(Path(input_dir).rglob(pattern))
    # Total files
    total_files = len(files)

    for i, file in enumerate(files):
        # File name
        filename = file.stem
        # Source of the data
        parts = file.parts
        source = parts[parts.index("raw") + 1]
        # Year of the data
        year = file.parent.name
        # Output folder
        output_folder  = os.path.join(output_dir, source, year)
        # Output file
        output_file = os.path.join(output_folder, filename)
        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        if os.path.exists(output_file):

            log_msg = (
                f"\n - Processing file : {i+1}/{total_files}\n"
                f" - Source          : {source}\n"
                f" - Year            : {year}\n"
                f" - File            : {filename}\n"
                f" - Status          : Already processed. Next..."
            )
            
            logging.info(log_msg)

            continue
    
        try: 

            with ZipFile(file, 'r') as z:
                z.extractall(output_folder)       
            
            log_msg = (
                f"\n - Processing file : {i+1}/{total_files}\n"
                f" - Source          : {source}\n"
                f" - Year            : {year}\n"
                f" - File            : {filename}\n"
                f" - Output          : {output_file}\n"
                f" - Status          : Done!"
            )
            
            logging.info("\n" + log_msg)

        except Exception as e:

            log_msg = (
                f"\n - Processing file : {i+1}/{total_files}\n"
                f" - Source          : {source}\n"
                f" - Year            : {year}\n"
                f" - File            : {filename}\n"
                f" - Reason          : {e}"
            )

            logging.error(log_msg)

        if i+1 == total_files:
            logging.info("All files are processed!")

# test
extract_raw_to_staging(input_dir='data\\raw', output_dir='data\\staging\\')


