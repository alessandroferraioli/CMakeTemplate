from Generator.base_generator import BaseGenerator
from DataClass.configuration import Configuration
import os


class CMakePresetGenerator(BaseGenerator):
    
    def __init__(self,config: Configuration) -> None:
        super().__init__(config)
        
    def generate(self)->None:
        
        #Copying Presets
       self._file_manager.copy_file(os.path.join(self._template_folder_name,"CMakePresets.json"),os.path.join(self._project_path,"CMakePresets.json"))

    
        
    
        
        

