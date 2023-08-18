from abc import ABC,abstractmethod
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
    
    def generate_template(self,file_in_path: str, file_out_path: str, new_str_replace: str, str_to_be_replaced: str = "#project_name#") ->None:
        file_in = open(file_in_path, "rt")
        file_out = open(file_out_path, "wt")
        for line in file_in:
            file_out.write(line.replace(str_to_be_replaced, new_str_replace))

        file_in.close()
        file_out.close()
        
        

