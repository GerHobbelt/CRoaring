from conans import ConanFile


class CRoaringConan(ConanFile):
    name = "croaring"
    version = "1.1.2"
    url = "https://github.com/Esri/CRoaring/tree/runtimecore"
    license = "https://github.com/Esri/CRoaring/blob/runtimecore/LICENSE"
    description = "Compressed bitmaps in C (and C++)."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/CRoaring/"

        # headers
        self.copy("*.h", src=base + "include", dst=relative + "include")

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
