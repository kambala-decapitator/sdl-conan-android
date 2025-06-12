from conan import ConanFile

required_conan_version = ">=2"

class SDLPrimitives(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = ["sdl/3.2.6"]
