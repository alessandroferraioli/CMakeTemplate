# CMakeTemplate

This simple script helps you creating a _hello world_ project using the following [configuration file](configuration.json). It allows you to configure the project as _libary/exectuable_ and as _conan/not conan_ project based.

## Configuration parameters
The configuration parameters are self-explanatory.
- ```project_name``` : The name of the project.
- ```project_directory```: Where the project will be created.
- ```author_email```: Email of the author.
- ```is_library```: Init the cmake project as library or as exectuable.
- ```is_conan```: Init the project using Conan.
- ```conan_dependencies```: The list of conan dependencies - Specify a name, version and path (if needed)

## How to use 
Just runs the following command:
```python
python template_generator.py
```


