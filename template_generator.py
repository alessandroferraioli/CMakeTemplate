import os
import shutil
import json

from configuration import Configuration,ConanPackage
from typing import List

def str2bool (val):
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))
    
def generate_template_string_list(file_in_path: str, file_out_path: str, new_str_replace: List[str], str_to_be_replaced: List[str] ):

    file_in = open(file_in_path, "rt")
    file_out = open(file_out_path, "wt")
    for line in file_in:
        for i,old_str in str_to_be_replaced:
            tmp_new_string = new_str_replace[i]
        file_out.write(line.replace(old_str, tmp_new_string))

    file_in.close()
    file_out.close()

    
def generate_template(file_in_path: str, file_out_path: str, new_str_replace: str, str_to_be_replaced: str = "#project_name#"):

    file_in = open(file_in_path, "rt")
    file_out = open(file_out_path, "wt")
    for line in file_in:
        file_out.write(line.replace(str_to_be_replaced, new_str_replace))

    file_in.close()
    file_out.close()


def create_folder(path: str):
    # Creating folder directiory
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)


template_folder_name = "TemplateFolder"

# Opening JSON file
config_file = open('configuration.json')
  
config = json.load(config_file)

# User Input - Project to create
project_name = config["project_name"]
project_directory =  config["project_directory"]
project_path = os.path.join(project_directory, project_name)

create_conan_project = str2bool(config["is_conan"])
is_library = str2bool(config["is_library"])



# Template files
cmake_file_name = "CMakeListsExe.txt"

if create_conan_project:
    cmake_file_name = "CMakeListsConanLib.txt" if is_library  else "CMakeListsConanExe.txt"
else:
    cmake_file_name = "CMakeListsLib.txt" if is_library  else "CMakeListsExe.txt"

        
cmake_template_path = os.path.join(template_folder_name, cmake_file_name) 
src_template_path = os.path.join(template_folder_name, "src")
include_template_path = os.path.join(template_folder_name, "include")
cmake_helper_template_path = os.path.join(template_folder_name, "cmake")


cmake_project_path = os.path.join(project_path, "CMakeLists.txt")
src_project_path = os.path.join(project_path, "src")
include_project_path = os.path.join(project_path, "include")
cmake_helper_path = os.path.join(project_path, "cmake")

# Creating folder project
create_folder(project_path)
create_folder(src_project_path)



# Copying cmake helper files
if create_conan_project:
    shutil.copytree(cmake_helper_template_path, cmake_helper_path)
    generate_template(file_in_path=os.path.join(template_folder_name,"conanfile.py"),
                      file_out_path=os.path.join(project_path,"conanfile.py"),
                      new_str_replace=project_name)

#Copying include folder 
#shutil.copytree(include_template_path, include_project_path)

#Copying cmakepreset
shutil.copy(os.path.join(template_folder_name,"CMakePresets.json"),os.path.join(project_path,"CMakePresets.json"))


#Generating Cmake
generate_template(file_in_path=cmake_template_path,
                  file_out_path=cmake_project_path, new_str_replace=project_name)

#Generating main.cpp
generate_template(file_in_path=os.path.join(src_template_path,"main.cpp"),
                  file_out_path=os.path.join(src_project_path,"main.cpp"),
                  new_str_replace=project_name)




def main():
    print("Started Template Generator")  
    config = Configuration(**json.load(open('configuration.json')))

if __name__ == '__main__':
    main()