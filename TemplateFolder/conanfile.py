from conans import ConanFile, CMake, tools


class #project_name#Conan(ConanFile):
    name = "#project_name#"
    license = "Proprietary"
    author = "#author_email"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}



    generators = "cmake", "cmake_find_package"

    #requires#

    build_requires = ["gtest/cci.20210126"]


    exports_sources = ["src*", "include*", "CMakeLists.txt"]

    _cmake = None
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC


    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        # place to configure extra staff
        self._cmake.configure()
        return self._cmake
    
        

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["#project_name#"]
        
        
    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.so*", "", "lib")
        self.copy("license*", dst="licenses", folder=True, ignore_case=True)



