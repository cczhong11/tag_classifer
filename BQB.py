import os
from Mover.FileMover import FileMover
from Filter.GeneralFilter import GeneralFilter
from pathlib import Path
PATH = str(Path(__file__).parent.absolute())

def main():
    general_filter = GeneralFilter(f"{PATH}/filter_file/bqb.yaml")
    mover = FileMover(path="/Users/tczhong/Pictures/bqb/orgranized")
    
    for filename in os.listdir(mover.base_folder):
        if os.path.isdir(f"{mover.base_folder}/{filename}"):
            continue
        
        tag = general_filter.filter(filename)
        if tag is None:
            continue
        mover.move(filename, tag)
        
        
if __name__ == "__main__":
    main()