from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration
import os


class GTestGenerator(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        self._file_template = "TestTemplate.cpp"
        
    def generate(self)->None:
        test_template_path = os.path.join(self._template_folder_name, "tests")
        template_path = os.path.join(test_template_path, self._file_template) 
        test_project_path = os.path.join(self._project_path, "test")
        name_file_project = "Test"+self._config.project_name+".cpp"
        file_project_path = os.path.join(test_project_path,name_file_project)

        self._file_manager.create_folder(test_project_path)
        self._file_manager.copy_file(template_path,file_project_path)
        self._file_manager.copy_file(os.path.join(test_template_path,"main.cpp"),os.path.join(test_project_path,"main.cpp"))
        self.generate_template(os.path.join(test_template_path,"CMakeLists.txt"),os.path.join(test_project_path,"CMakeLists.txt"),self._project_name)
    
        
    
        
        

