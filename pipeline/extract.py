# Library
import src

# The command below simply extract files (zip) from the raw folder to the staging folder
src.extract_to_landing(
    input_dir='data\\raw', 
    output_dir='data\\landing', 
    pattern='*.zip'
)
