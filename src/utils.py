from pathlib import Path
from typing import List, Dict, Union
from typing import Any, TypeVar
from extract_office_content import ExtractOfficeContent

import pathlib
import pickle
import re

def clean_data(text: List):
    ...

def clean_more_data(text: List): 
    ...

def process_data(extractor, files : List[Union[str, pathlib.Path]]) -> Dict:
    # Assuming the extractor is ExtractOfficeContent object
    output = {}
    ommited = []
    for file in files:
        try:
            tmp_prep = extractor(file)
            output[file] = tmp_prep
        except Exception as e: 
            print(e)
            ommited.append(file)
            continue
    print(f"Number of processed files: \n {len(output.keys())}")
    print(f"Number of ommited files: \n {len(ommited)}")
    return output


def save_files(files: Union[Dict, List], outpath: Union[str, pathlib.Path]) -> None:
    with open(outpath, 'wb') as outfile:
        pickle.dump(files, outfile)

def load_file(path: Union[str, pathlib.Path]) -> None:
    with open(path, 'rb') as outfile:
        data = pickle.load(outfile)
    return data

