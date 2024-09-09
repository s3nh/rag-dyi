import sys
sys.path.insert(0, '../')

import argparse
from src.utils import process_data, clean_data, clean_more_data
import extract_office_content
from extract_office_content import ExtractOfficeContent

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type = str)
    args = parser.parse_args()
    return args

def check_files(files) -> bool:
    assert len(files) > 0, 'Number of files should be greater than 0'


def main():
    args = get_args()
    print(args.files)

    extractor = ExtractOfficeContent()

if __name__ == '__main__':
    main()