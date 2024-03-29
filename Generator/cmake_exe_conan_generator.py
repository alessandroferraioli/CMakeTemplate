from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration

import os
import shutil


class CmakeGeneratorExeConan(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._cmake_template_filename = "CMakeListsConanExe.txt"
        
    def generate(self)->None:
        cmake_template_path = os.path.join(self._template_folder_name, self._cmake_template_filename) 
        cmake_project_path = os.path.join(self._project_path, "CMakeLists.txt")
        

        self.generate_template(file_in_path= cmake_template_path,
                               file_out_path=cmake_project_path,
                               new_str_replace=[self._config.project_name])
        

    
        
    
        
        

