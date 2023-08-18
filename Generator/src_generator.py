from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration
import os
import shutil


class SrcGenerator(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._file_template = "main.cpp"
        
    def generate(self)->None:
        src_template_path = os.path.join(self._template_folder_name, "src")
        template_path = os.path.join(src_template_path, self._file_template) 
        src_project_path = os.path.join(self._project_path, "src")
        file_project_path = os.path.join(src_project_path, "main.cpp")

        self._folder_generator.generate(src_project_path)
        self.generate_template(file_in_path= template_path,
                               file_out_path=file_project_path,
                               new_str_replace=[self._config.project_name])
    
        
    
        
        

