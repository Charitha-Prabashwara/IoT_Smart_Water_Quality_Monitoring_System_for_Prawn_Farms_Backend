from .Repository import Repository

class BackgroundTempRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "background_temp"
        self._create_if_notExist()


   