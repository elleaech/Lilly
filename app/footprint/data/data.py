class IData:
    @property
    def json(self):
        return self.__dict__