import os
import shutil
import json

from configuration import Configuration
from base_generator import BaseGenerator
from FactoryGenerator import Factory
from typing import List



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