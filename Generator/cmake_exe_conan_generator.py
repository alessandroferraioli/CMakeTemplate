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
        cmake_helper_template_path = os.path.join(self._template_folder_name, "cmake","conan_helper.cmake")
        cmake_helper_project_path = os.path.join(self._project_path,"cmake","conan_helper.cmake")
        cmake_project_path = os.path.join(self._project_path, "CMakeLists.txt")
        
        #Generating the folder
        self._folder_generator.generate(self._project_path)
        self._folder_generator.generate(os.path.join(self._project_path,"cmake"))

        shutil.copy(cmake_helper_template_path,cmake_helper_project_path)
        
        str_dep = self._config.getDependenciesString()
        
        self.generate_template(file_in_path=os.path.join(self._template_folder_name,"conanfile.py"),
                      file_out_path=os.path.join(self._project_path,"conanfile.py"),
                      new_str_replace=[self._config.project_name,str_dep],str_to_be_replaced=["#project_name#","#requires#"])
        
        #Copying Presets
        shutil.copy(os.path.join(self._template_folder_name,"CMakePresets.json"),os.path.join(self._project_path,"CMakePresets.json"))


        self.generate_template(file_in_path= cmake_template_path,
                               file_out_path=cmake_project_path,
                               new_str_replace=[self._config.project_name])
        

    
        
    
        
        

