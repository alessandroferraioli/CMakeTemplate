from Generator.base_generator import BaseGenerator
from Generator.cmake_exe_conan_generator import CmakeGeneratorExeConan
from Generator.cmake_exe_generator import CmakeGeneratorExe
from Generator.cmake_lib_conan_generator import CmakeGeneratorLibConan
from Generator.cmake_lib_generator import CmakeGeneratorLib
from Generator.src_generator import SrcGenerator
from Generator.gtest_generator import GTestGenerator
from Generator.conan_generator import ConanGenerator
from Generator.cmake_preset_generator import CMakePresetGenerator

from DataClass.configuration import Configuration

from typing import List
class Factory:
    
    def __init__(self,config:Configuration) -> None:
        self._config = config
        
    def GetGenerators(self)->List[BaseGenerator]:
        result : List[BaseGenerator] = []
        
        generator : BaseGenerator = None
        if self._config.is_library == True:
            generator = CmakeGeneratorLibConan(self._config) if self._config.is_conan == True else CmakeGeneratorLib(self._config)
        else:      
            generator = CmakeGeneratorExeConan(self._config) if self._config.is_conan == True else CmakeGeneratorExe(self._config)
            
        generator._file_manager.create_folder(generator._project_path)

        
        result.append(generator)
        result.append(SrcGenerator(self._config))
        
        if self._config.is_conan == True:
            result.append(ConanGenerator(self._config))
            
        if self._config.use_gtest == True:
            result.append(GTestGenerator(self._config))
            
        result.append(CMakePresetGenerator(self._config))
        
        return result
        
        
        