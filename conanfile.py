from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.env import VirtualBuildEnv
import os

required_conan_version = ">=2"

class SDLPrimitives(ConanFile):
    name = "sdl_primitives"
    version = "1.0"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = ["sdl/3.2.6"]

    _android_project_dir = "android-app"
    package_folder = f"{os.getcwd()}/{_android_project_dir}/app/src/main/jniLibs"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        env = VirtualBuildEnv(self)
        venv = env.environment()
        sdl = self.dependencies.host["sdl"]
        venv.define("ORG_GRADLE_PROJECT_SDL_JAR_PATH",
                    os.path.join(sdl.package_folder, "share", "java", "SDL3", f"SDL3-{sdl.ref.version}.jar"))
        env.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

        # build Android project
        gradleWrapper = "gradlew.bat" if self.settings_build.os == "Windows" else "./gradlew"
        self.run(f"{gradleWrapper} assembleDebug", cwd=os.path.join(self.source_folder, self._android_project_dir))
