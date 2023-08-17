import os
import shutil

class FolderGenerator:
    
    def __init__(self) -> None:
        pass
    
    
    def generate(self,path:str)->None:
        if os.path.exists(path):
            shutil.rmtree(path)

        os.mkdir(path)