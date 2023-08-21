import json

from DataClass.configuration import Configuration
from Generator.base_generator import BaseGenerator
from Generator.FactoryGenerator import Factory
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