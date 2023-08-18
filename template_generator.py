import os
import shutil
import json

from configuration import Configuration
from base_generator import BaseGenerator
from FactoryGenerator import Factory
from typing import List


    
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



def main():
    print("Started Template Generator")  
    config = Configuration(**json.load(open('configuration.json')))
    factory: Factory = Factory(config)
    generators : List[BaseGenerator] = factory.GetGenerators()
    for gen in generators:
        gen.generate()
    
    print("Generation Completed")
    
if __name__ == '__main__':
    main()