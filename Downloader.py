import os
from Mover.FileMover import FileMover
from GeneralFilter import GeneralFilter
from pathlib import Path
PATH = str(Path(__file__).parent.absolute())

def main():
    general_filter = GeneralFilter(f"{PATH}/filter_file/download.yaml")
    home_path = os.path.expanduser("~")
    mover = FileMover(path=f"{home_path}/Downloads")
    
    for filename in os.listdir(mover.base_folder):
        if os.path.isdir(f"{mover.base_folder}/{filename}"):
            continue
        
        tag = general_filter.filter(filename)
        if tag is None:
            continue
        mover.move(filename, tag)
        
        
if __name__ == "__main__":
    main()