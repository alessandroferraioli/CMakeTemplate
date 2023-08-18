from base_generator import BaseGenerator
from configuration import Configuration

import os
import shutil


class SrcGenerator(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._file_template = "main.cpp"
        
    def generate(self) -> bool:
        template_path = os.path.join(self._template_folder_name, self._file_template) 
        file_project_path = os.path.join(self._project_path, "main.cpp")
        

        self.generate_template(file_in_path= template_path,
                               file_out_path=file_project_path,
                               new_str_replace=self._config.project_name)
    
        
    
        
        

