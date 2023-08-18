from base_generator import BaseGenerator
from cmake_exe_conan_generator import CmakeGeneratorExeConan
from cmake_exe_generator import CmakeGeneratorExe
from cmake_lib_conan_generator import CmakeGeneratorLibConan
from cmake_lib_generator import CmakeGeneratorLib
from src_generator import SrcGenerator
from configuration import Configuration

from typing import List
class Factory:
    
    def __init__(self,config:Configuration) -> None:
        self._config = config
        
    def GetGenerator(self)->List[BaseGenerator]:
        result : List[BaseGenerator] = []
        
        generator : BaseGenerator = None
        if self._config.is_library:
            generator = CmakeGeneratorLibConan(self._config) if self._config.is_conan == True else CmakeGeneratorLib(self._config)
        else:      
            generator = CmakeGeneratorExeConan(self._config) if self._config.is_conan == True else CmakeGeneratorExe(self._config)

        
        result.append(generator)
        result.append(SrcGenerator(self._config))
        
        
        