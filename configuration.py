from dataclasses import dataclass
from typing import List


@dataclass
class ConanPackage:
    name:str
    version:str
    path:str


@dataclass
class Configuration:
    project_name:str
    project_directory:str
    is_library:bool
    is_conan:bool
    conan_dependencies:List[ConanPackage]
    
    
    

    