from conans import ConanFile, tools
import os


class DataframeConan(ConanFile):
    name = "DataFrame"
    version = "0.1.2"
    description = "C++ implementation of dataframe"
    topics = ("conan", "dataframe")
    url = "https://github.com/lukaszlaszko/conan-dataframe"
    homepage = "https://github.com/fairtide/DataFrame"
    author = "Shadow <bincrafters@gmail.com>"
    license = "Apache-2.0"
    no_copy_source = True

    exports = ["LICENSE.md"]

    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/fairtide/DataFrame"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
