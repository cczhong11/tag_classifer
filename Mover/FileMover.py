from .MoverBase import MoverBase, log_decorator_info
import os 
import shutil

class FileMover(MoverBase):
    def __init__(self, path):
        super(FileMover, self).__init__(path)
    
    @log_decorator_info
    def move(self, filename, tag):
        new_folder = f"{self.base_folder}/{tag}"
        original_filename = filename
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        new_file = f"{self.base_folder}/{tag}/{filename}"
        
        if os.path.exists(new_file):
            subfix = filename.split(".")[-1]
            filename_text = filename.split(".")[0]
            index = filename_text.split("_")[-1]
            if index.isdigit():
                new_index = int(index)+1
            else:
                new_index = 1
            if "_" in filename:
                filename = "_".join(filename_text.split("_")[:-1])+"_"+str(new_index)+"."+subfix
            else:
                filename = f"{filename_text}_{new_index}"+"."+subfix
            new_file = f"{self.base_folder}/{tag}/{filename}"
            
        shutil.move(f"{self.base_folder}/{original_filename}", new_file)