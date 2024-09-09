import os
import pathlib
from src.utils import process_data, save_files
from extract_office_content import ExtractOfficeContent

def main():
    file_path: str = 'knowledge-base'
    print(os.listdir(file_path))
    # Do we want to exclude any files?
    files = list(pathlib.Path(file_path).rglob('*.*'))
    print(f"Number of files {len(files)}")
    extractor = ExtractOfficeContent()
    output: Dict = process_data(extractor = extractor, files = files)
    print(output)
    save_files(output, 'example_output.pkl')

if __name__ == '__main__':
    main()
