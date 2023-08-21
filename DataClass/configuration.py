from dataclasses import dataclass
from typing import List


@dataclass
class ConanPackage:
    name:str
    version:str
    path:str
    
    def getString(self)->str:
        result = f"{self.name}/{self.version}"
        if self.path != "":
            result += f"@{self.path}"
            
        return result
            


@dataclass
class Configuration:
    project_name:str
    project_directory:str
    author_email:str
    is_library:bool
    is_conan:bool
    conan_dependencies:List[ConanPackage]
    
    
    def getDependenciesString(self)->str:
        result = ''
        for idx,dep_dict ,in enumerate(self.conan_dependencies):
            dep:ConanPackage = ConanPackage(**dep_dict)
            result += f'\"{dep.getString()}\"'
            if(idx+1 < len(self.conan_dependencies)):
                result+=","
        return result
    
    
    

    