from .utils import *


class Template:
    @property
    def template(self):
        return self.__template

    @property
    def __filename(self):
        return "p4j-config.json"

    def __init__(self, **kwargs):
        if not kwargs:
            self.load_from_file()
        else:
            self.__template = kwargs

    def load_from_file(self):
        self.__template = load_file(self.__filename)
        validate(self.__template)
