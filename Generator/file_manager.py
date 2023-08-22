import os
import shutil

class FileManager:
    
    def __init__(self) -> None:
        pass
    
    
    def create_folder(self,path:str)->None:
        if os.path.exists(path):
            shutil.rmtree(path)

        os.mkdir(path)
        
    def copy_file(self,src_path:str,dest_path:str)->None:
        shutil.copyfile(src_path,dest_path)
        
    def copy_tree(self,src_path:str,dest_path:str)->None:
        shutil.copytree(src_path, dest_path)