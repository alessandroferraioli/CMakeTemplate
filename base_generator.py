from abc import ABC,abstractmethod
from typing import List
import os

from configuration import Configuration
from  folder_generator import FolderGenerator

class BaseGenerator(ABC):
    
    def __init__(self,config: Configuration) -> None:
        self._config = config
        self._template_folder_name = "TemplateFolder"
        self._project_name = config.project_name
        self._project_directory =  config.project_directory
        self._project_path = os.path.join(self._project_directory,self._project_name)
        
        self._folder_generator = FolderGenerator()
        
    @abstractmethod 
    def generate(self)->None:
        pass
    
    def generate_template(self,file_in_path: str, file_out_path: str, new_str_replace: List[str], str_to_be_replaced: List[str] = ["#project_name#"]) ->None:
        file_in = open(file_in_path, "rt")
        file_out = open(file_out_path, "wt")
        for line in file_in:
            found :bool  = False
            for idx,old_str in enumerate(str_to_be_replaced):
                if old_str in line:
                    file_out.write(line.replace(old_str, new_str_replace[idx]))
                    found = True
            if not found:
                file_out.write(line)

        file_in.close()
        file_out.close()
    

        

