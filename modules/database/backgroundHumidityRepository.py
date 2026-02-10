from .Repository import Repository

class BackgroundHumidityRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "background_humidity"
        self._create_if_notExist()


   