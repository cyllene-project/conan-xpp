from conans import ConanFile, CMake, tools


class XppConan(ConanFile):
    name = "xpp"
    version = "1.4.0"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/polybar/xpp.git")

    def package(self):
        self.copy("*.hpp")
