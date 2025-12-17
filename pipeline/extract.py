# Library
import src

# The command below simply extract files (zip) from the raw folder to the staging folder
src.extract_raw_to_staging(
    input_dir='data\\raw', 
    output_dir='data\\staging', 
    pattern='*.zip'
)
