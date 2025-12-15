import os
from zipfile import ZipFile
from pathlib import Path

def raw_to_bronze(input_dir: str, output_dir: str, pattern = '*'):
    """
    input_dir: aaaa
    output_dir: bbbb
    pattern: cccc
    """
    
    os.makedirs(output_dir, exist_ok=True)
    files = list(Path(input_dir).rglob(pattern))
    total_files = len(files)

    for i, file in enumerate(files):

        filename = os.path.basename(file).removesuffix('.zip')
        output_file = os.path.join(output_dir, filename)

        if i == total_files:
            print('\nAll files are processed!')

        if os.path.exists(output_file):
            print(f'\nFile already processed: {filename}')
            print('Next...')
            continue

        print(f'\nProcessing : {filename}')
        z = ZipFile(file, 'r')
        z.extractall(output_dir)
        print(f'Output     : {output_file}')

        if i == total_files:
            print('\nAll files are processed!')
