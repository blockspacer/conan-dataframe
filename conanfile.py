from conans import ConanFile, tools
import os


class DataFrameConan(ConanFile):
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

    requires = (
        "snappy/1.1.7@bincrafters/stable",
        "lz4/1.8.3@bincrafters/stable",
        "rapidjson/1.1.0@bincrafters/stable",
        "mongo-c-driver/1.11.0@bisect/stable",
        "mongo-cxx-driver/3.3.0@bisect/stable",
        "arrow/0.13.0@shadow/stable"
    )

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
