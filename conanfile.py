from conans import ConanFile, tools


class UtilitylibConan(ConanFile):
    name = "utility-lib"
    version = "0.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Utilitylib here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "*.sln", "*.cpp", "*.hpp", "*.vcxproj", "*.filters"

    def build(self):
        build_command = tools.msvc_build_command(self.settings, "utility-lib.sln", targets=["utility-lib"])
        self.run(build_command)

    def package(self):
        self.copy("*.hpp", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        tools.collect_libs(self)
