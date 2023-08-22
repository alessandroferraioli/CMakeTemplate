from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration

import os
import shutil


class ConanGenerator(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._conan_template_filename = "conanfile.py"
        
    def generate(self)->None:
        
        cmake_helper_template_path = os.path.join(self._template_folder_name, "cmake","conan_helper.cmake")
        cmake_helper_project_path = os.path.join(self._project_path,"cmake","conan_helper.cmake")
        
        #Generating the folder

        self._file_manager.create_folder(os.path.join(self._project_path,"cmake"))

        self._file_manager.copy_file(cmake_helper_template_path,cmake_helper_project_path)
        
        str_dep = self._config.getDependenciesString()
        
        self.generate_template(file_in_path=os.path.join(self._template_folder_name,"conanfile.py"),
                      file_out_path=os.path.join(self._project_path,"conanfile.py"),
                      new_str_replace=[self._config.project_name,str_dep,self._config.author_email],str_to_be_replaced=["#project_name#","#requires#","#author_email#"])



    
        
    
        
        

