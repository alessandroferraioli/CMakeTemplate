from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration

import os
import shutil


class CmakeGeneratorLib(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._cmake_template_filename = "CMakeListsLib.txt"
        
    def generate(self)->None:
        cmake_template_path = os.path.join(self._template_folder_name, self._cmake_template_filename) 
        cmake_project_path = os.path.join(self._project_path, "CMakeLists.txt")
        
        #Generating the folder
        self._file_manager.create_folder(self._project_path)
        
        #Copying Presets
        shutil.copy(os.path.join(self._template_folder_name,"CMakePresets.json"),os.path.join(self._project_path,"CMakePresets.json"))


        self.generate_template(file_in_path= cmake_template_path,
                               file_out_path=cmake_project_path,
                               new_str_replace=[self._config.project_name])
    
        
    
        
        

